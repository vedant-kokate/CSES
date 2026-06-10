data = STDIN.read.split.map(&:to_i)
return if data.empty?

n = data[0]
x = data[1]
count = 0
sum_ = 0
dp = Hash.new(0)
dp[0] = 1

index = 2
n.times do
  sum_ += data[index]
  count += dp[sum_ - x]
  dp[sum_] += 1
  index += 1
end

puts count
