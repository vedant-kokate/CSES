a = STDIN.gets
b = STDIN.gets
return if a.nil? || b.nil?
a.chomp!
b.chomp!
n = a.length
m = b.length
dp = Array.new(n + 1) { Array.new(m + 1, 0) }

(0..n).each do |i|
  dp[i][0] = i
end

(0..m).each do |j|
  dp[0][j] = j
end

(1..n).each do |i|
  (1..m).each do |j|
    if a[i - 1] != b[j - 1]
      dp[i][j] = 1 + [dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]].min
    else
      dp[i][j] = dp[i - 1][j - 1]
    end
  end
end

puts dp[n][m]
