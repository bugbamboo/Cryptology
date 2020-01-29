import java.util.Scanner;
//Uses Library from Kristian Lundkvist (kristian.lundkvist@gmail.com) for getting random data from ANU Quantum Random Number Server (https://qrng.anu.edu.au)
public class QuantumCrypto{
        public static void main(String[] args){
                Scanner sc =new Scanner(System.in);
                String plaintext = sc.next();
                int n =plaintext.length();


                anurandom random = new anurandom(n);
                byte[] key = random.getBytes();
                byte[] pt = plaintext.getBytes();
                byte[] ct= new byte[n];
                byte[] pttest= new byte[n];

              for(int x=0;x<n;x++){
                      ct[x]=(byte)(pt[x]^key[x]);
              }

             for(int y=0;y<n;y++){
                pttest[y]=(byte)(ct[y]^key[y]);
            }
            String s2 = new String(pttest);



            String s = new String(ct);
            System.out.println(s);
            System.out.println(s2);

        }
