im

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);

        int t2=sc.nextInt();

        while(t2>0){


         int n=sc.nextInt();
         int k=sc.nextInt();
         int q=sc.nextInt();

         List<Integer> li=new ArrayList<>();
         int count=0;

         for(int i=0;i<n;i++){

            int tem=sc.nextInt();
            if(tem<=q){
                count++;
                if(i==n-1)
                li.add(count);
            }else{
                li.add(count);
                count=0;
            }
         }

         long ans=0;

         //System.out.println(li);
         for(int i=0;i<li.size();i++){

            int cons=li.get(i);

            for(int j=1;j<=cons;j++){
                int plus=j+k;
                plus--;
                if(plus<=cons){

                    long ways=cons-plus;
                    ways++;
                    ans+=ways;
                }
            }
         }
         System.out.println(ans);
            t2--;
        }

    }
}