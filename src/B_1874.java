import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class B_1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        int count = 0;
        int curr = 1;

        while(count < n){
            int target = Integer.parseInt(br.readLine());
            if(!stack.isEmpty() && target < stack.peek()){
                System.out.println("NO");
                return;
            }
            while(stack.isEmpty() || stack.peek() != target){
                stack.push(curr++);
                sb.append("+\n");
            }
            stack.pop();
            sb.append("-\n");

            count++;
        }
        System.out.println(sb);

    }
}
