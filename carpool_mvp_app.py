import streamlit as st
import pandas as pd

# 假设这是一个占位符函数，模拟调用 Maps API
# 在实际运行时，你需要用真实工具替代
def find_carpool_route(origin, destination, waypoints):
    """
    模拟调用 Maps API 计算多点路线。
    由于 Streamlit 环境不能直接调用外部 API 工具，我们使用一个虚构的函数来展示结果。
    """
    if not origin or not destination:
        return None, None, None
        
    # --- 这里是你的数据科学和 API 调用的核心逻辑 ---
    
    # 假设 API 返回的计算结果
    import random
    base_distance = random.randint(150, 400) # km
    base_duration = random.randint(150, 300) # minutes
    
    # 根据途经点数量增加绕路距离和时间
    if waypoints:
        num_waypoints = len(waypoints)
        extra_distance = num_waypoints * random.randint(5, 20)
        extra_duration = num_waypoints * random.randint(10, 30)
        
        total_distance = f"{base_distance + extra_distance} 公里"
        total_duration = f"{int((base_duration + extra_duration) / 60)} 小时 {int((base_duration + extra_duration) % 60)} 分钟"
    else:
        total_distance = f"{base_distance} 公里"
        total_duration = f"{int(base_duration / 60)} 小时 {int(base_duration % 60)} 分钟"
        
    # 模拟地图链接（实际地图API会返回真实的URL）
    map_url = "https://example.com/map/view_route" 
        
    return total_distance, total_duration, map_url


# --- Streamlit 界面 ---

st.set_page_config(page_title="简易拼车行程计算器", layout="wide")

st.title("🚗 城际拼车行程计算器 (MVP)")
st.markdown("---")

st.header("1. 行程路线输入")

# 使用 form 结构收集数据，统一提交
with st.form("carpool_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        origin = st.text_input("📍 司机出发地 (起点)", placeholder="例如：深圳市南山区科技园")
    
    with col2:
        destination = st.text_input("🏁 最终目的地", placeholder="例如：广州白云国际机场")

    st.subheader("2. 途经点/乘客接送点 (选填)")
    
    # 允许多个途经点输入，用逗号分隔
    waypoints_input = st.text_area("中途接送点 (用逗号分隔)", 
                                   placeholder="例如：东莞市虎门站, 广州南站")

    submitted = st.form_submit_button("📐 计算最佳路线")

if submitted:
    if not origin or not destination:
        st.error("请输入完整的起点和终点！")
    else:
        # 清理途经点输入
        waypoints_list = [w.strip() for w in waypoints_input.split(',') if w.strip()]
        
        st.subheader("--- 计算结果 ---")
        
        with st.spinner("正在调用路径优化算法..."):
            # 调用核心计算函数
            distance, duration, map_link = find_carpool_route(origin, destination, waypoints_list)
        
        if distance:
            st.success("✅ 路线计算成功！")
            
            # 显示关键数据
            st.metric("总行程距离", distance)
            st.metric("预计总耗时", duration)
            
            # 显示途经点信息
            if waypoints_list:
                st.info(f"包含 {len(waypoints_list)} 个途经点：{', '.join(waypoints_list)}")
            
            st.markdown(f"**[点击查看详细地图路线 (模拟链接)]({map_link})**")
        else:
            st.error("计算失败，请检查地址输入是否有效。")