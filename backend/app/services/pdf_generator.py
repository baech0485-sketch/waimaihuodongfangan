# -*- coding: utf-8 -*-
"""
外卖活动方案PDF生成器
呈尚策划 品牌定制
"""

import sys
import os
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from datetime import datetime

# ==================== 配色方案 ====================
COLORS = {
    'brand_dark': HexColor('#1A1A2E'),
    'brand_gold': HexColor('#C9A962'),
    'eleme_blue': HexColor('#0097FF'),
    'eleme_dark': HexColor('#0078CC'),
    'eleme_light': HexColor('#E6F4FF'),
    'meituan_yellow': HexColor('#FFCA28'),
    'meituan_dark': HexColor('#F5A623'),
    'meituan_light': HexColor('#FFF8E1'),
    'text_dark': HexColor('#1A1A2E'),
    'text_medium': HexColor('#4A5568'),
    'text_light': HexColor('#718096'),
    'bg_light': HexColor('#F7FAFC'),
    'border': HexColor('#E2E8F0'),
    'accent': HexColor('#048A81'),
    'success': HexColor('#38A169'),
}

PAGE_WIDTH = 21 * cm

# ==================== 活动数据 ====================
ELEME_ACTIVITIES = [
    ['活动名称', '活动设置', '目的说明'],
    ['爆单红包', '通用红包 | 40元以下商家补贴5元', '获取平台流量扶持，提升店铺曝光'],
    ['减配送费', '减4-5元 | 达到店铺免配送', '降低下单门槛，提升转化率'],
    ['优评返券', '满20减2元', '刺激顾客好评，提升评分和曝光'],
    ['下单返券', '满20减2元', '促进二次消费，提升复购率'],
    ['集点返券', '30天内下3单返3元无门槛券', '培养老客忠诚度，提升店铺权重'],
]

ELEME_DETAILS = [
    ("爆单红包", "报名通用红包，订单40元以下商家补贴5元，获得平台流量入口曝光机会"),
    ("减配送费", "减免4-5元配送费，使顾客实付配送费接近0元，消除顾客下单顾虑"),
    ("优评返券", "顾客给出好评后自动发放满20减2元优惠券，激励好评提升店铺评分"),
    ("下单返券", "顾客完成订单后自动发放满20减2元优惠券，促进顾客二次下单"),
    ("集点返券", "30天内累计下单3次返3元无门槛券，培养老客户消费习惯，提升权重"),
]

MEITUAN_ACTIVITIES = [
    ['活动名称', '活动设置', '目的说明'],
    ['天天神券', '普通神券5元', '获取平台流量扶持，提升店铺曝光'],
    ['减配送费', '减4-5元 | 达到店铺免配送', '降低下单门槛，提升转化率'],
    ['好评返券', '满20减2元', '刺激顾客好评，提升评分和曝光'],
    ['下单返券', '满20减2元', '促进二次消费，提升复购率'],
    ['集点返券', '30天内下3单返3元无门槛券', '培养老客忠诚度，提升店铺权重'],
]

MEITUAN_DETAILS = [
    ("天天神券", "报名普通神券5元，获得美团首页神券入口流量，大幅提升曝光"),
    ("减配送费", "减免4-5元配送费，使顾客实付配送费接近0元，消除顾客下单顾虑"),
    ("好评返券", "顾客给出好评后自动发放满20减2元优惠券，激励好评提升店铺评分"),
    ("下单返券", "顾客完成订单后自动发放满20减2元优惠券，促进顾客二次下单"),
    ("集点返券", "30天内累计下单3次返3元无门槛券，培养老客户消费习惯，提升权重"),
]

TIPS = [
    ("合理定价", "确保菜品定价已包含活动成本，保证每单利润"),
    ("活动报名", "每月月初完成当月活动报名，确保活动连续性"),
    ("数据监控", "每周查看平台数据报表，关注各活动投入产出比"),
    ("避免叠加", "注意活动叠加规则，防止过度让利导致亏损"),
    ("定期复盘", "每月进行活动效果复盘，根据数据优化配置"),
]


def register_chinese_fonts():
    """注册中文字体"""
    font_options = [
        ("C:/Windows/Fonts/msyh.ttc", "MSYH"),
        ("C:/Windows/Fonts/simhei.ttf", "SimHei"),
        ("/System/Library/Fonts/PingFang.ttc", "PingFang"),
        ("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", "WQY"),
    ]
    for font_path, font_name in font_options:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont(font_name, font_path))
                return font_name
            except:
                continue
    return "Helvetica"


def draw_brand_header(c, current_y, font_name):
    """绘制呈尚策划品牌头部"""
    header_height = 25 * mm
    current_y -= header_height
    c.setFillColor(COLORS['brand_dark'])
    c.rect(0, current_y, PAGE_WIDTH, header_height, fill=True, stroke=False)
    c.setStrokeColor(COLORS['brand_gold'])
    c.setLineWidth(1.5)
    c.line(20*mm, current_y + 3*mm, PAGE_WIDTH - 20*mm, current_y + 3*mm)
    c.setFillColor(white)
    c.setFont(font_name, 18)
    c.drawCentredString(PAGE_WIDTH/2, current_y + 14*mm, "呈尚策划")
    c.setFillColor(COLORS['brand_gold'])
    c.setFont(font_name, 9)
    c.drawCentredString(PAGE_WIDTH/2, current_y + 6*mm, "专业外卖代运营服务商")
    c.setFillColor(COLORS['brand_gold'])
    c.circle(15*mm, current_y + 12*mm, 2*mm, fill=True, stroke=False)
    c.circle(PAGE_WIDTH - 15*mm, current_y + 12*mm, 2*mm, fill=True, stroke=False)
    return current_y


def draw_brand_footer(c, current_y, store_name, font_name):
    """绘制呈尚策划品牌底部"""
    footer_height = 20 * mm
    c.setFillColor(COLORS['brand_dark'])
    c.rect(0, current_y - footer_height, PAGE_WIDTH, footer_height, fill=True, stroke=False)
    c.setStrokeColor(COLORS['brand_gold'])
    c.setLineWidth(1)
    c.line(20*mm, current_y - 3*mm, PAGE_WIDTH - 20*mm, current_y - 3*mm)
    c.setFillColor(white)
    c.setFont(font_name, 11)
    c.drawCentredString(PAGE_WIDTH/2, current_y - 10*mm, "呈尚策划 | 让外卖运营更简单")
    c.setFillColor(COLORS['brand_gold'])
    c.setFont(font_name, 8)
    c.drawString(20*mm, current_y - 16*mm, f"店铺: {store_name}")
    c.drawRightString(PAGE_WIDTH - 20*mm, current_y - 16*mm, f"制定日期: {datetime.now().strftime('%Y-%m-%d')}")
    return current_y - footer_height


def draw_platform_banner(c, current_y, platform, font_name):
    """绘制平台横幅"""
    margin_x = 1.5 * cm
    content_width = PAGE_WIDTH - 2 * margin_x
    banner_height = 18 * mm
    current_y -= banner_height
    if platform == 'eleme':
        color = COLORS['eleme_blue']
        text = "饿了么平台活动方案"
    else:
        color = COLORS['meituan_yellow']
        text = "美团平台活动方案"
    c.setFillColor(color)
    c.roundRect(margin_x, current_y, content_width, banner_height, 8, fill=True, stroke=False)
    c.setFillColor(white if platform == 'eleme' else COLORS['text_dark'])
    c.setFont(font_name, 16)
    c.drawCentredString(PAGE_WIDTH/2, current_y + 6*mm, text)
    return current_y


def draw_store_name(c, current_y, store_name, font_name):
    """绘制店铺名称"""
    current_y -= 8 * mm
    c.setFillColor(COLORS['text_dark'])
    c.setFont(font_name, 14)
    c.drawCentredString(PAGE_WIDTH/2, current_y, store_name)
    return current_y


def draw_divider(c, current_y, platform):
    """绘制分割线"""
    margin_x = 1.5 * cm
    current_y -= 15 * mm
    primary_color = COLORS['eleme_blue'] if platform == 'eleme' else COLORS['meituan_yellow']
    c.setFillColor(primary_color)
    c.circle(margin_x + 4*mm, current_y + 4*mm, 2.5*mm, fill=True, stroke=False)
    c.setStrokeColor(COLORS['border'])
    c.setLineWidth(0.8)
    c.line(margin_x + 12*mm, current_y + 4*mm, PAGE_WIDTH - margin_x - 12*mm, current_y + 4*mm)
    c.setFillColor(COLORS['accent'])
    c.circle(PAGE_WIDTH - margin_x - 4*mm, current_y + 4*mm, 2.5*mm, fill=True, stroke=False)
    return current_y


def draw_section_title(c, current_y, title, font_name, platform):
    """绘制章节标题"""
    margin_x = 1.5 * cm
    current_y -= 15 * mm
    color = COLORS['eleme_dark'] if platform == 'eleme' else COLORS['meituan_dark']
    c.setFillColor(color)
    c.setFont(font_name, 14)
    c.drawString(margin_x, current_y, title)
    return current_y


def draw_activity_table(c, current_y, activities, platform, font_name):
    """绘制活动表格"""
    margin_x = 1.5 * cm
    current_y -= 12 * mm
    if platform == 'eleme':
        header_color = COLORS['eleme_blue']
        alt_color = COLORS['eleme_light']
    else:
        header_color = COLORS['meituan_yellow']
        alt_color = COLORS['meituan_light']
    col_widths = [3*cm, 7*cm, 6*cm]
    row_height = 12 * mm
    table_x = margin_x + 1*cm
    for i, row in enumerate(activities):
        row_y = current_y - i * row_height
        if i == 0:
            c.setFillColor(header_color)
        elif i % 2 == 1:
            c.setFillColor(white)
        else:
            c.setFillColor(alt_color)
        c.rect(table_x, row_y - row_height, sum(col_widths), row_height, fill=True, stroke=False)
        c.setStrokeColor(COLORS['border'])
        c.setLineWidth(0.5)
        c.rect(table_x, row_y - row_height, sum(col_widths), row_height, fill=False, stroke=True)
        x_offset = table_x
        for w in col_widths[:-1]:
            x_offset += w
            c.line(x_offset, row_y, x_offset, row_y - row_height)
        if i == 0:
            c.setFillColor(white if platform == 'eleme' else COLORS['text_dark'])
        else:
            c.setFillColor(COLORS['text_dark'])
        c.setFont(font_name, 10)
        x_offset = table_x
        for j, (cell, w) in enumerate(zip(row, col_widths)):
            c.drawCentredString(x_offset + w/2, row_y - row_height/2 - 3*mm, cell)
            x_offset += w
    return current_y - len(activities) * row_height


def draw_activity_details(c, current_y, details, platform, font_name):
    """绘制活动详解"""
    margin_x = 1.5 * cm
    current_y -= 10 * mm
    primary_color = COLORS['eleme_blue'] if platform == 'eleme' else COLORS['meituan_yellow']
    for title, desc in details:
        c.setFillColor(primary_color)
        c.roundRect(margin_x, current_y - 5*mm, 18*mm, 7*mm, 3, fill=True, stroke=False)
        c.setFillColor(white if platform == 'eleme' else COLORS['text_dark'])
        c.setFont(font_name, 9)
        c.drawCentredString(margin_x + 9*mm, current_y - 3*mm, title)
        c.setFillColor(COLORS['text_medium'])
        c.setFont(font_name, 10)
        c.drawString(margin_x + 22*mm, current_y - 3*mm, desc)
        current_y -= 12 * mm
    return current_y


def draw_effects(c, current_y, platform, font_name):
    """绘制效果预期"""
    margin_x = 1.5 * cm
    content_width = PAGE_WIDTH - 2 * margin_x
    current_y -= 12 * mm
    effects = [
        ('曝光量提升', '30%-50%', COLORS['eleme_blue'] if platform == 'eleme' else COLORS['meituan_yellow']),
        ('转化率提升', '15%-25%', COLORS['accent']),
        ('复购率提升', '20%-30%', COLORS['success']),
        ('评分维护', '稳步提升', COLORS['brand_gold']),
    ]
    card_width = (content_width - 3*8*mm) / 4
    card_height = 20 * mm
    for i, (label, value, color) in enumerate(effects):
        card_x = margin_x + i * (card_width + 8*mm)
        c.setFillColor(COLORS['bg_light'])
        c.roundRect(card_x, current_y - card_height, card_width, card_height, 5, fill=True, stroke=False)
        c.setFillColor(color)
        c.rect(card_x, current_y - 4*mm, card_width, 4*mm, fill=True, stroke=False)
        c.setFont(font_name, 14)
        c.drawCentredString(card_x + card_width/2, current_y - 12*mm, value)
        c.setFillColor(COLORS['text_light'])
        c.setFont(font_name, 8)
        c.drawCentredString(card_x + card_width/2, current_y - 18*mm, label)
    return current_y - card_height


def draw_tips(c, current_y, platform, font_name):
    """绘制执行建议"""
    margin_x = 1.5 * cm
    current_y -= 10 * mm
    primary_color = COLORS['eleme_blue'] if platform == 'eleme' else COLORS['meituan_yellow']
    for i, (title, desc) in enumerate(TIPS):
        c.setFillColor(primary_color)
        c.circle(margin_x + 4*mm, current_y - 2*mm, 3*mm, fill=True, stroke=False)
        c.setFillColor(white if platform == 'eleme' else COLORS['text_dark'])
        c.setFont(font_name, 8)
        c.drawCentredString(margin_x + 4*mm, current_y - 4*mm, str(i+1))
        c.setFillColor(COLORS['text_dark'])
        c.setFont(font_name, 10)
        c.drawString(margin_x + 12*mm, current_y - 3*mm, f"{title}:")
        c.setFillColor(COLORS['text_medium'])
        c.drawString(margin_x + 12*mm + len(title)*5*mm + 8*mm, current_y - 3*mm, desc)
        current_y -= 10 * mm
    return current_y


def generate_single_platform_pdf(store_name, platform, output_path):
    """生成单平台活动方案PDF"""
    font_name = register_chinese_fonts()
    page_height = 55 * cm

    # 第一遍：计算实际内容高度
    c = canvas.Canvas(output_path, pagesize=(PAGE_WIDTH, page_height))
    current_y = page_height - 1 * cm

    current_y = draw_brand_header(c, current_y, font_name)
    current_y -= 12 * mm
    current_y = draw_platform_banner(c, current_y, platform, font_name)
    current_y = draw_store_name(c, current_y, store_name, font_name)
    current_y = draw_divider(c, current_y, platform)

    activities = ELEME_ACTIVITIES if platform == 'eleme' else MEITUAN_ACTIVITIES
    details = ELEME_DETAILS if platform == 'eleme' else MEITUAN_DETAILS

    current_y = draw_section_title(c, current_y, "一、活动配置总览", font_name, platform)
    current_y = draw_activity_table(c, current_y, activities, platform, font_name)
    current_y -= 15 * mm

    current_y = draw_section_title(c, current_y, "二、活动配置详解", font_name, platform)
    current_y = draw_activity_details(c, current_y, details, platform, font_name)
    current_y -= 10 * mm

    current_y = draw_section_title(c, current_y, "三、效果预期", font_name, platform)
    current_y = draw_effects(c, current_y, platform, font_name)
    current_y -= 18 * mm

    current_y = draw_section_title(c, current_y, "四、执行建议", font_name, platform)
    current_y = draw_tips(c, current_y, platform, font_name)
    current_y -= 15 * mm

    actual_height = page_height - current_y + 20 * mm + 1 * cm

    # 第二遍：使用正确高度生成PDF
    c = canvas.Canvas(output_path, pagesize=(PAGE_WIDTH, actual_height))
    current_y = actual_height - 1 * cm

    current_y = draw_brand_header(c, current_y, font_name)
    current_y -= 12 * mm
    current_y = draw_platform_banner(c, current_y, platform, font_name)
    current_y = draw_store_name(c, current_y, store_name, font_name)
    current_y = draw_divider(c, current_y, platform)

    current_y = draw_section_title(c, current_y, "一、活动配置总览", font_name, platform)
    current_y = draw_activity_table(c, current_y, activities, platform, font_name)
    current_y -= 15 * mm

    current_y = draw_section_title(c, current_y, "二、活动配置详解", font_name, platform)
    current_y = draw_activity_details(c, current_y, details, platform, font_name)
    current_y -= 10 * mm

    current_y = draw_section_title(c, current_y, "三、效果预期", font_name, platform)
    current_y = draw_effects(c, current_y, platform, font_name)
    current_y -= 18 * mm

    current_y = draw_section_title(c, current_y, "四、执行建议", font_name, platform)
    current_y = draw_tips(c, current_y, platform, font_name)
    current_y -= 15 * mm

    draw_brand_footer(c, current_y, store_name, font_name)
    c.save()
    return output_path


def generate_both_platforms_pdf(store_name, output_path):
    """生成双平台活动方案PDF"""
    font_name = register_chinese_fonts()
    page_height = 95 * cm

    c = canvas.Canvas(output_path, pagesize=(PAGE_WIDTH, page_height))
    current_y = page_height - 1 * cm

    current_y = draw_brand_header(c, current_y, font_name)
    current_y -= 12 * mm

    # 饿了么部分
    current_y = draw_platform_banner(c, current_y, 'eleme', font_name)
    current_y = draw_store_name(c, current_y, store_name, font_name)
    current_y = draw_divider(c, current_y, 'eleme')
    current_y = draw_section_title(c, current_y, "一、活动配置总览", font_name, 'eleme')
    current_y = draw_activity_table(c, current_y, ELEME_ACTIVITIES, 'eleme', font_name)
    current_y -= 15 * mm
    current_y = draw_section_title(c, current_y, "二、活动配置详解", font_name, 'eleme')
    current_y = draw_activity_details(c, current_y, ELEME_DETAILS, 'eleme', font_name)
    current_y -= 20 * mm

    # 美团部分
    current_y = draw_platform_banner(c, current_y, 'meituan', font_name)
    current_y = draw_store_name(c, current_y, store_name, font_name)
    current_y = draw_divider(c, current_y, 'meituan')
    current_y = draw_section_title(c, current_y, "一、活动配置总览", font_name, 'meituan')
    current_y = draw_activity_table(c, current_y, MEITUAN_ACTIVITIES, 'meituan', font_name)
    current_y -= 15 * mm
    current_y = draw_section_title(c, current_y, "二、活动配置详解", font_name, 'meituan')
    current_y = draw_activity_details(c, current_y, MEITUAN_DETAILS, 'meituan', font_name)
    current_y -= 20 * mm

    # 通用部分
    current_y = draw_section_title(c, current_y, "三、效果预期", font_name, 'eleme')
    current_y = draw_effects(c, current_y, 'eleme', font_name)
    current_y -= 18 * mm
    current_y = draw_section_title(c, current_y, "四、执行建议", font_name, 'eleme')
    current_y = draw_tips(c, current_y, 'eleme', font_name)
    current_y -= 15 * mm

    actual_height = page_height - current_y + 20 * mm + 1 * cm

    # 第二遍渲染双平台
    c = canvas.Canvas(output_path, pagesize=(PAGE_WIDTH, actual_height))
    current_y = actual_height - 1 * cm
    current_y = draw_brand_header(c, current_y, font_name)
    current_y -= 12 * mm

    # 饿了么部分
    current_y = draw_platform_banner(c, current_y, 'eleme', font_name)
    current_y = draw_store_name(c, current_y, store_name, font_name)
    current_y = draw_divider(c, current_y, 'eleme')
    current_y = draw_section_title(c, current_y, "一、活动配置总览", font_name, 'eleme')
    current_y = draw_activity_table(c, current_y, ELEME_ACTIVITIES, 'eleme', font_name)
    current_y -= 15 * mm
    current_y = draw_section_title(c, current_y, "二、活动配置详解", font_name, 'eleme')
    current_y = draw_activity_details(c, current_y, ELEME_DETAILS, 'eleme', font_name)
    current_y -= 20 * mm

    # 美团部分
    current_y = draw_platform_banner(c, current_y, 'meituan', font_name)
    current_y = draw_store_name(c, current_y, store_name, font_name)
    current_y = draw_divider(c, current_y, 'meituan')
    current_y = draw_section_title(c, current_y, "一、活动配置总览", font_name, 'meituan')
    current_y = draw_activity_table(c, current_y, MEITUAN_ACTIVITIES, 'meituan', font_name)
    current_y -= 15 * mm
    current_y = draw_section_title(c, current_y, "二、活动配置详解", font_name, 'meituan')
    current_y = draw_activity_details(c, current_y, MEITUAN_DETAILS, 'meituan', font_name)
    current_y -= 20 * mm

    # 通用部分
    current_y = draw_section_title(c, current_y, "三、效果预期", font_name, 'eleme')
    current_y = draw_effects(c, current_y, 'eleme', font_name)
    current_y -= 18 * mm
    current_y = draw_section_title(c, current_y, "四、执行建议", font_name, 'eleme')
    current_y = draw_tips(c, current_y, 'eleme', font_name)
    current_y -= 15 * mm

    draw_brand_footer(c, current_y, store_name, font_name)
    c.save()
    return output_path


def generate_plan(store_name: str, platform: str, output_dir: str = ".") -> str:
    """
    生成外卖活动方案PDF

    Args:
        store_name: 店铺名称
        platform: 平台类型 ('eleme', 'meituan', 'both')
        output_dir: 输出目录

    Returns:
        生成的PDF文件路径
    """
    os.makedirs(output_dir, exist_ok=True)

    platform_names = {
        'eleme': '饿了么',
        'meituan': '美团',
        'both': '双平台'
    }
    platform_name = platform_names.get(platform, platform)

    # 清理文件名中的非法字符
    safe_store_name = store_name.replace('/', '_').replace('\\', '_').replace(':', '_')
    filename = f"{safe_store_name}_{platform_name}活动方案.pdf"
    output_path = os.path.join(output_dir, filename)

    if platform == 'both':
        generate_both_platforms_pdf(store_name, output_path)
    else:
        generate_single_platform_pdf(store_name, platform, output_path)

    print(f"[OK] PDF已生成: {output_path}")
    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python pdf_generator.py <店铺名> <平台> [输出目录]")
        print("平台: eleme | meituan | both")
        print("示例: python pdf_generator.py \"逸莹麻辣串串香\" eleme ./output")
        sys.exit(1)

    store = sys.argv[1]
    plat = sys.argv[2]
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "."

    if plat not in ['eleme', 'meituan', 'both']:
        print(f"错误: 无效的平台 '{plat}'，请使用 eleme, meituan 或 both")
        sys.exit(1)

    generate_plan(store, plat, out_dir)
