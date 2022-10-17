class Solution {
public:
    
    vector<pair<int, int>> dir {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    struct Point{
        int row = 0;
        int col = 0;
        
        Point(int row, int col){
            this -> row = row;
            this -> col = col;
        }
        
        Point(){
            
        }
        
    };
    
    // check if point has valid coordinates
    bool isValid(vector<vector<int>>& grid, Point& c){
        if(c.row >= 0 && c.col >= 0 && c.row < grid.size() && c.col < grid[0].size())
            return true;
        return false;
    }
    
    void bfs(int row, int col, vector<vector<int>>& grid){
        unordered_set<int> v;
        deque<pair<Point, int>> q;
        
        Point temp;
        pair<Point, int> current;
        int rowc, colc, temp_hash;
        int m = grid[0].size();
        
        q.push_back(pair(Point(row, col), 0));
        v.insert(row * m + col);
        
        while(q.size() != 0){
            // pop current
            current = q.front();
            q.pop_front();
            
            // unwrap for easier use
            rowc = current.first.row;
            colc = current.first.col;
            
            // set value of when the orange will become rotten
            if(grid[rowc][colc] == 1)
                grid[rowc][colc] = -current.second;
            else
                grid[rowc][colc] = max(grid[rowc][colc], -current.second);

            // add to queue next cells
            for(auto& modifier: dir){
                temp = Point(rowc + modifier.first, colc + modifier.second);
                temp_hash = temp.row * m + temp.col;
                if(isValid(grid, temp) && (grid[temp.row][temp.col] == 1 || grid[temp.row][temp.col] < 0) && v.find(temp_hash) == v.end()){
                    v.insert(temp_hash);
                    q.push_back(pair(temp, current.second + 1));
                }
            }
            
        }
    }
    
    int orangesRotting(vector<vector<int>>& grid) {
        int result = 0;
        for(int i = 0; i < grid.size(); ++i){
            for(int j = 0; j < grid[0].size(); ++j){
                if(grid[i][j] == 2)
                    bfs(i, j, grid);
            }
        }
        
        for(int i = 0; i < grid.size(); ++i){
            for(int j = 0; j < grid[0].size(); ++j){
                if(grid[i][j] == 1)
                    return -1;
                result = min(result, grid[i][j]);
            }
        }
        return -result;
    }
};
