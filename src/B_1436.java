import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B_1436 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 1;  // N번째 큰 수 
        int start = 666;    // 가장 작은 저주받은 수
        while(count < n){
            String numStr = Integer.toString(++start);
            // 연속된 세 숫자가 모두 6인지 확인
            for(int i = 0; i < numStr.length() - 2;i++){
                if(numStr.charAt(i) == '6' && numStr.charAt(i+1) == '6' && numStr.charAt(i+2) == '6'){
                    count++;
                    break;
                }
            }
        }
        System.out.println(start);
    }
}
