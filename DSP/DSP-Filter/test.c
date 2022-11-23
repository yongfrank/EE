#include <stdio.h>
#include <math.h>
/*
SOS Matrix:                                                  
1  2  1  1  -1.7193929141691948  0.8610574795347461          
1  2  1  1  -1.5237898734101736  0.64933827386370635         
1  2  1  1  -1.4017399331200424  0.51723237044751591         
1  2  1  1  -1.3435020629061745  0.45419615396638446         

Scale Values:                                                
0.035416141341387819                                         
0.031387100113383172                                         
0.028873109331868367                                         
0.027673522765052503  
做如下转换：
1.缩放
[1  2  1] * 0.035416141341387819
[1  2  1] * 0.031387100113383172
[1  2  1] * 0.028873109331868367
[1  2  1] * 0.027673522765052503
得到：
[0.035416141341387819  2*0.035416141341387819  0.035416141341387819]
[0.031387100113383172  2*0.031387100113383172  0.031387100113383172] 
[0.028873109331868367  2*0.028873109331868367  0.028873109331868367] 
[0.027673522765052503  2*0.027673522765052503  0.027673522765052503]
2.舍掉第四列参数
3.将后两列分别乘以-1，即：
0.035416141341387819  2*0.035416141341387819  0.035416141341387819  -1.7193929141691948  0.8610574795347461          
0.031387100113383172  2*0.031387100113383172  0.031387100113383172  -1.5237898734101736  0.64933827386370635         
0.028873109331868367  2*0.028873109331868367  0.028873109331868367  -1.4017399331200424  0.51723237044751591         
0.027673522765052503  2*0.027673522765052503  0.027673522765052503  -1.3435020629061745  0.45419615396638446 
这样就得到了滤波器系数组了
*/
#define IIR_SECTION 4                /*见前面设计输出为4个SOS块*/
#include <stdint.h>
#include <stdio.h>
#include <float.h>
#include <arm_mve.h>
/**
 *  *S       ：指向浮点Biquad级联结构的实例.
 *  *pSrc    ：指向输入数据块。
 *  *pDst    ：指向输出数据块。
 *  blockSize：每次调用要处理的样本数。
 *  返回值    ：无.
 */

/*
*作用      :初始化滤波器
*S        :指向浮点SOS级联结构的实例。
*numStages:滤波器中二阶SOS的数量
*pCoeffs  :滤波器参数指针,参数按下列顺序存储
*          {b10, b11, b12, a11, a12, b20, b21, b22, a21, a22, ...}
*pState   :历史状态缓冲区指针
*/
void arm_biquad_cascade_df1_init_f32(
        arm_biquad_casd_df1_inst_f32 * S,
        uint8_t numStages,
  const float32_t * pCoeffs,
        float32_t * pState)
{
  /* Assign filter stages */
  S->numStages = numStages;

  /* Assign coefficient pointer */
  S->pCoeffs = pCoeffs;

  /* Clear state buffer and size is always 4 * numStages */
  memset(pState, 0, (4U * (uint32_t) numStages) * sizeof(float32_t));

  /* Assign state pointer */
  S->pState = pState;
}

typedef struct
{
  unsigned int numStages; /*2阶节的个数，应为2*numStages.        */
  float *pState;          /*状态系数数组指针，数组长度为4*numStages*/
  float *pCoeffs;         /*系数数组指针， 数组的长度为5*numStages.*/
} arm_biquad_casd_df1_inst_f32;

void arm_biquad_cascade_df1_f32(
  const arm_biquad_casd_df1_inst_f32 * S,
  float * pSrc,
  float * pDst,
  unsigned int blockSize)
{
  float *pIn = pSrc;                         /*源指针     */
  float *pOut = pDst;                        /*目的指针    */
  float *pState = S->pState;                 /*状态指针    */
  float *pCoeffs = S->pCoeffs;               /*参数指针    */
  float acc;                                 /*累加器      */
  float b0, b1, b2, a1, a2;                  /*滤波器参数   */
  float Xn1, Xn2, Yn1, Yn2;                  /*滤波器状态变量*/
  float Xn;                                  /*临时输入     */
  unsigned int sample, stage = S->numStages; /*循环计数     */

  do
  {
    /* Reading the coefficients */
    b0 = *pCoeffs++;
    b1 = *pCoeffs++;
    b2 = *pCoeffs++;
    a1 = *pCoeffs++;
    a2 = *pCoeffs++;

    Xn1 = pState[0];
    Xn2 = pState[1];
    Yn1 = pState[2];
    Yn2 = pState[3];

    sample = blockSize >> 2u;

    while(sample > 0u)
    {
      /* 读第一个输入 */
      Xn = *pIn++;

      /* acc =  b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] + a1 * y[n-1] + a2 * y[n-2] */
      Yn2 = (b0 * Xn) + (b1 * Xn1) + (b2 * Xn2) + (a1 * Yn1) + (a2 * Yn2);

      /* Store the result in the accumulator in the destination buffer. */
      *pOut++ = Yn2;

      /* 每次计算输出后，状态都应更新. */
      /* 状态应更新为:  */
      /* Xn2 = Xn1    */
      /* Xn1 = Xn     */
      /* Yn2 = Yn1    */
      /* Yn1 = acc   */

      /* Read the second input */
      Xn2 = *pIn++;

      /* acc =  b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] + a1 * y[n-1] + a2 * y[n-2] */
      Yn1 = (b0 * Xn2) + (b1 * Xn) + (b2 * Xn1) + (a1 * Yn2) + (a2 * Yn1);

      /* 将结果存储在目标缓冲区的累加器中. */
      *pOut++ = Yn1;

      /* 每次计算输出后，状态都应更新. */
      /* 状态应更新为:  */
      /* Xn2 = Xn1    */
      /* Xn1 = Xn     */
      /* Yn2 = Yn1    */
      /* Yn1 = acc   */

      /*读第三个输入 */
      Xn1 = *pIn++;

      /* acc =  b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] + a1 * y[n-1] + a2 * y[n-2] */
      Yn2 = (b0 * Xn1) + (b1 * Xn2) + (b2 * Xn) + (a1 * Yn1) + (a2 * Yn2);

      /* 将结果存储在目标缓冲区的累加器中. */
      *pOut++ = Yn2;

      /* 每次计算输出后，状态都应更新. */
      /* 状态应更新为: */
      /* Xn2 = Xn1    */
      /* Xn1 = Xn     */
      /* Yn2 = Yn1    */
      /* Yn1 = acc   */
      /* 读第四个输入 */
      Xn = *pIn++;

      /* acc =  b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] + a1 * y[n-1] + a2 * y[n-2] */
      Yn1 = (b0 * Xn) + (b1 * Xn1) + (b2 * Xn2) + (a1 * Yn2) + (a2 * Yn1);

      /* 将结果存储在目标缓冲区的累加器中. */
      *pOut++ = Yn1;

      /* 每次计算输出后，状态都应更新. */
      /* 状态应更新为:  */
      /* Xn2 = Xn1    */
      /* Xn1 = Xn     */
      /* Yn2 = Yn1    */
      /* Yn1 = acc   */
      Xn2 = Xn1;
      Xn1 = Xn;

      /* 递减循环计数器 */
      sample--;
    }

    /* 如果blockSize不是4的倍数，
    *请在此处计算任何剩余的输出样本。
    *不使用循环展开. */
    sample = blockSize & 0x3u;

    while(sample > 0u)
    {
      /* 读取输入 */
      Xn = *pIn++;

      /* acc =  b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] + a1 * y[n-1] + a2 * y[n-2] */
      acc = (b0 * Xn) + (b1 * Xn1) + (b2 * Xn2) + (a1 * Yn1) + (a2 * Yn2);

      /* 将结果存储在目标缓冲区的累加器中. */
      *pOut++ = acc;

      /* 每次计算输出后，状态都应更新。 */
      /* 状态应更新为:    */
      /* Xn2 = Xn1    */
      /* Xn1 = Xn     */
      /* Yn2 = Yn1    */
      /* Yn1 = acc   */
      Xn2 = Xn1;
      Xn1 = Xn;
      Yn2 = Yn1;
      Yn1 = acc;

      /* d递减循环计数器 */
      sample--;
    }

    /*  将更新后的状态变量存储回pState数组中 */
    *pState++ = Xn1;
    *pState++ = Xn2;
    *pState++ = Yn1;
    *pState++ = Yn2;

    /*第一阶段从输入缓冲区到输出缓冲区.     */
    /*随后的numStages在输出缓冲区中就地发生*/
    pIn = pDst;

    /* 重置输出指针 */
    pOut = pDst;

    /* 递减循环计数器 */
    stage--;

  } while(stage > 0u);
}

static float iir_state[4*IIR_SECTION];/*历史状态缓冲区         */
const float iir_coeffs[5*IIR_SECTION]={
    0.035416141341387819,2*0.035416141341387819,0.035416141341387819,1.7193929141691948,-0.8610574795347461,    0.031387100113383172,2*0.031387100113383172,0.031387100113383172,1.5237898734101736,-0.64933827386370635,    0.028873109331868367,2*0.028873109331868367,0.028873109331868367,1.4017399331200424,-0.51723237044751591,    0.027673522765052503,2*0.027673522765052503,0.027673522765052503,1.3435020629061745,-0.45419615396638446
};
static arm_biquad_casd_df1_inst_f32 S;
/*假定采样512个点*/
#define BUF_SIZE 512
#define PI 3.1415926
#define SAMPLE_RATE  32000 /*32000Hz*/
int main()
{
    float raw[BUF_SIZE];
    float raw_4k[BUF_SIZE];
    float raw_out[BUF_SIZE];

    float raw_noise[BUF_SIZE];
    float raw_noise_out[BUF_SIZE];

    arm_biquad_casd_df1_inst_f32 S;
    FILE *pFile=fopen("./simulation.csv","wt+");
    if(pFile==NULL)
    {
        printf("file opened failed");
        return -1;
    }

    for(int i=0;i<BUF_SIZE;i++)
    {
        /*模拟800Hz正弦幅度171，叠加幅度50随机噪声 */
        raw[i] = 0.5*1024.0/3*sin(2*PI*800*i/32000.0f)+rand()%50;
        raw_4k[i] = 0.5*1024.0/3*sin(2*PI*4000*i/32000.0f);
        /*模拟800Hz +4000Hz+随机噪声叠加输入      */
        raw_noise[i] = raw[i] + raw_4k[i];
    }
    /*初始化滤波器，以及滤波*/
    arm_biquad_cascade_df1_init_f32(&S, IIR_SECTION, (float *)&iir_coeffs[0], (float *)&iir_state[0]);
    arm_biquad_cascade_df1_f32(&S, raw, raw_out, BUF_SIZE);

    for(int i=0;i<BUF_SIZE;i++)
    {
       fprintf(pFile,"%f,",raw[i]);
    }

    fprintf(pFile,"\n");
    for(int i=0;i<BUF_SIZE;i++)
    {
        fprintf(pFile,"%f,",raw_4k[i]);
    }
    fprintf(pFile,"\n");
    for(int i=0;i<BUF_SIZE;i++)
    {
        fprintf(pFile,"%f,",raw_out[i]);
    }

    /*初始化滤波器，以及滤波*/
    arm_biquad_cascade_df1_init_f32(&S, IIR_SECTION, (float *)&iir_coeffs[0], (float *)&iir_state[0]);
    arm_biquad_cascade_df1_f32(&S, raw_noise, raw_noise_out, BUF_SIZE);

    fprintf(pFile,"\n");
    for(int i=0;i<BUF_SIZE;i++)
    {
        fprintf(pFile,"%f,",raw_noise[i]);
    }

    fprintf(pFile,"\n");
    for(int i=0;i<BUF_SIZE;i++)
    {
        fprintf(pFile,"%f,",raw_noise_out[i]);
    }

    fclose(pFile);

    return 0;
}