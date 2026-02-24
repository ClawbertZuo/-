import math

test_weight=float(input('你的物品有多重？（按kg为单位）'))


def get_billing_weight(weight):
    """通用的计费重量计算：向上取整到 0.5kg 的倍数"""
    return math.ceil(weight * 2) / 2

def get_rainbow_plus(weight):
    """彩虹桥 Plus线 (日本仓)"""
    if weight <= 0.1: return 800
    
    bw = get_billing_weight(weight)
    prices = {
        0.5: 800, 1.0: 1600, 1.5: 2400, 2.0: 3200, 2.5: 4000,
        3.0: 4900, 3.5: 5600, 4.0: 6400, 4.5: 7200, 5.0: 8000
    }
    # 表格显示通常上限为3kg，但给出了5kg的报价
    return prices.get(bw, "超过5kg报价范围")

def get_rainbow_special(weight):
    """彩虹桥 专线 (日本仓)"""
    if weight <= 0.1: return 900
    
    bw = get_billing_weight(weight)
    prices = {
        0.5: 900, 1.0: 1700, 1.5: 2500, 2.0: 3300, 2.5: 4100,
        3.0: 4900, 3.5: 5700, 4.0: 6500, 4.5: 7300, 5.0: 8100
    }
    return prices.get(bw, "超过5kg报价范围")

def get_rainbow_lite(weight):
    """彩虹桥 Lite线 (日本仓) - 严格限重 2.5kg"""
    if weight > 2.5: return "超重！实重上限 2.5kg"
    
    bw = get_billing_weight(weight)
    prices = {
        0.5: 800, 1.0: 1300, 1.5: 1800, 2.0: 2300, 2.5: 2800
    }
    return prices.get(bw, "不支持或无报价")

def get_paper_plane_jp(weight):
    """纸飞机 (日本仓) - 上限 30kg"""
    if weight > 30: return "超重！实重上限 30kg"
    if weight <= 0.1: return 590
    
    bw = get_billing_weight(weight)
    prices = {
        0.5: 750, 1.0: 950, 1.5: 1200, 2.0: 1450, 2.5: 1700,
        3.0: 1950, 3.5: 2450, 4.0: 2950, 4.5: 3450, 5.0: 3950
    }
    
    if bw <= 5.0:
        return prices[bw]
    else:
        # 5kg 后，每增加 0.5kg 价格加 500
        extra_steps = (bw - 5.0) / 0.5
        return int(3950 + extra_steps * 500)




# --- 测试用例 ---
print(f"重量 {test_weight}kg (计费重 3.0kg) 的运费：")
print(f"彩虹桥 Plus线: {get_rainbow_plus(test_weight)}")
print(f"彩虹桥 Lite线: {get_rainbow_lite(test_weight)}")
print(f"纸飞机(日本): {get_paper_plane_jp(test_weight)}")
print(f"彩虹桥专线: {get_rainbow_special(test_weight)}")
