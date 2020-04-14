#include<math.h>
#include<stdio.h>
int main()
{
    int t;
    scanf("%lld",&t);
    while(t--)
    {
        long int n;
        scanf("%lld",&n);
        int a[n],b[n],j=1;
        a[0]=-1,b[0]=1;
        for(long int i=0;i<n;i++)
            {
                long long int m;
                scanf("%lld",&m);
                if(m<0)
                m=0-m;
                if(m%2==0)
                {
                    if(m%4==0)
                    b[j]=0;
                    else b[j]=1;
                    a[j]=i;
                    j++;
                }
            }
        a[j]=n;
        long long int x=0;
        for(long int i=1;i<j;i++)
        {
            if(b[i]!=0)
            {
                long long int m=a[i]-a[i-1];
                long long int y=a[i+1]-a[i];
                y=y*m;
                x=x+y;
            }
        }
        long long int z=(n*(n+1))/2;
        printf("%lld\n",z-x);
    }
    return 0;
}