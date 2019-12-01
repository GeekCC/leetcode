#include<iostream>
#include<stack>
using namespace std;

int A[7]={4,5,7,3,9,6,2};
int Sum[7]={0};
stack<int> S;

//index 表示元素个数
//sum 表示要求的和
void makeSum(int index,int sum){
	if(sum==0){//满足条件，输出栈中的所有元素
		stack<int> temp=S;
		while(!temp.empty()){
			cout<<temp.top()<<" ";
			temp.pop();
		}
		cout<<endl;
		return;
	}
	for(int i=0;i<index && sum<=Sum[index-i-1];i++){
		if(A[index-i-1]<=sum){
			S.push(A[index-i-1]);//当前元素入栈
			makeSum(index-i-1,sum-A[index-i-1]);
			S.pop();
		}
	}		
}


int main(){
	Sum[0]=A[0];// Sum 用来计算前n项和，减少没必要的计算,但需要花费O(n)的空间
	for(int i=1;i<7;i++){
		Sum[i]=A[i]+Sum[i-1];
	}
	makeSum(7,15);
	return 0;
}