def operations(score, op)
  ops = {
    'C' => lambda { |score| score.pop() },
    'D' => lambda { |score| score.push(2 * (score[score.length() - 1]).to_i) },
    '+' => lambda { |score| score.push(score[score.length() - 1].to_i + score[score.length() - 2].to_i) }
  }

  if ops.has_key?(op)
    ops[op].call(score)
  else
    score.push(op.to_i)
  end

  return score 
end

def calPoints(ops)
  score = []
  
  ops.each do |op|
    operations(score, op)
  end

  return score.sum()
end

ops = ["5","2","C","D","+"]
ops2 = ["5","-2","4","C","D","9","+","+"]
ops3 = ["1","C"]
p calPoints(ops)
p calPoints(ops2)
p calPoints(ops3)
