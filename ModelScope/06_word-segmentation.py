from modelscope.pipelines import pipeline

word_segmentation = pipeline('word-segmentation')

inputs = ['今天天气不错，适合出去游玩','这本书很好，建议你看看']
print(word_segmentation(inputs))

# 输出
# [{'output': ['今天', '天气', '不错', '，', '适合', '出去', '游玩']}, {'output': ['这', '本', '书', '很', '好', '，', '建议', '你', '看看']}]
