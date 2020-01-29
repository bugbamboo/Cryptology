
import java.util.Arrays;
import java.util.Scanner;

public class QuantumCrypto2{
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
       int byteCount= sc.nextInt();
       byte[] pt = new byte[byteCount];
       for(int x=0; x<byteCount;x++){
           pt[x]=sc.nextByte(2);
       }




        anurandom random = new anurandom(byteCount);
        byte[] key = random.getBytes();

        byte[] ct= new byte[byteCount];


        for(int x=0;x<byteCount;x++){
            ct[x]=(byte)(pt[x]^key[x]);
        }


        System.out.println(Arrays.toString(ct));

    }
}
