import random

rules = """
复合句子 = 句子 , 连词 复合句子 | 句子
连词 = 而且 | 但是 | 不过 
句子 = 主语 谓语 宾语
主语 = 你| 我 | 他 
谓语 = 吃| 喝 | 玩 
宾语 = 桃子| 皮球 | 狗子 | 喵大人
"""


def get_grammer_by_description(description):
    rules_pattern = [r.split('=') for r in description.split('\n') if r.strip()]
    target_with_expend = [(t, ex.split('|')) for t, ex in rules_pattern]
    grammer = {t.strip(): [e.strip() for e in ex] for t, ex in target_with_expend}
    return grammer


def generate_by_grammer(grammer, target='句子'):  # 通过改变target 来达到改变生成效果
    if target not in grammer: return target
    return ''.join([generate_by_grammer(grammer, t) for t in random.choice(grammer[target]).split()])


if __name__ == '__main__':
    grammer = get_grammer_by_description(rules)
    print(generate_by_grammer(grammer))
    ret = generate_by_grammer(grammer, target='复合句子')
    print(ret)




