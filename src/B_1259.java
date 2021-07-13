import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B_1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 0이 나올 때까지 테스트 케이스 수행
        while(true){
            String number = br.readLine();
            if(Integer.parseInt(number) == 0){break;}

            String reverse = new StringBuilder(number).reverse().toString();
            if(number.equals(reverse)){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }

        }
    }
}
