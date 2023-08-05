from random import randint
from ayaka import AyakaCat, get_session
from .bag import get_money
from .utils import config

cat = AyakaCat("pray")
cat.help = '祈福'

all_wegiht = 0
for item in config.pray:
    all_wegiht += item.weight


def get_diff():
    target = randint(0, all_wegiht-1)
    print(target)

    sum = 0
    for item in config.pray:
        if sum <= target and sum+item.weight > target:
            return item.reward
        sum += item.weight

    raise


@cat.on_cmd(cmds=["pray", "祈祷"])
async def pray():
    '''为群里随机一人（除了自己）祈祷随机金币'''
    nodes = await cat.get_users()

    # 排除自己
    nodes = [node for node in nodes if node.id != cat.user.id]

    # 找到受害人
    node = nodes[randint(0, len(nodes)-1)]
    uid = node.id
    name = node.name

    prayer_name = cat.user.name

    diff = get_diff()
    with get_session() as session:
        money = get_money(session, cat.group.id, uid)
        money.money += diff
        session.commit()

    await cat.send(f"[{prayer_name}]的祈祷，让[{name}]获得 {diff}金")
    if diff < 0:
        await cat.send(f"反转了，[{name}]损失 {-diff}金")
    await cat.send(f"[{name}] 现在持有 {money.money}金")
