import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B_1018 {

    public static char[][] graph;
    public static int answer = 100000000;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        StringTokenizer st = new StringTokenizer((br.readLine()));

        int m, n;   // n * m 보드 크기
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 그래프 입력받기
        graph = new char[n][m];
        for(int i = 0; i < n; i++){
            String str = br.readLine();
            graph[i] = str.toCharArray();
        }

        // 8 * 8 체스판을 완전 탐색해본다.
        for(int i = 0; i < n-7; i ++){
            for(int j = 0; j < m-7; j++){
                int result = getnumOfRect(i, j);
                if (result < answer){
                    answer = result;
                }
            }
        }

        System.out.println(answer);
    }

    public static int getnumOfRect(int x, int y){
        int count = 0;
        char flag = graph[x][y];
        for(int i = x; i < x + 8; i++){
            for(int j = y; j < y +8; j++){
                if(graph[i][j] != flag){
                    count++;
                }
                // 반대 플래그로 전환
                flag = (flag == 'W') ? 'B': 'W';
            }
            // 행이 바뀔 때 반대 플래그로 전환
            flag = (flag == 'W') ? 'B': 'W';
        }
        // 처음 색 그대로 OR 맨 처음 색을 바꾸고 시작할 경우 중 최솟값
        return Math.min(count, 64 - count);

    }
}
