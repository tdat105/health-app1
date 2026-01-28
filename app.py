import streamlit as st
import time

st.set_page_config(page_title="NutriPod", layout="centered")

# =======================
# STATE
# =======================
if "step" not in st.session_state:
    st.session_state.step = 1

# =======================
# STYLE
# =======================
st.markdown("""
<style>
button {
    width: 100%;
    height: 55px;
    font-size: 18px !important;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# =======================
# SCREEN 1 – HOME
# =======================
if st.session_state.step == 1:
    st.title("👋 Xin chào, Thu!")

    st.markdown("🔥 **1.200 kcal còn lại hôm nay**")
    st.markdown("💧 2/8 ly nước  🍽️ 1 bữa đã dùng")

    st.subheader("🎯 Chọn mục tiêu")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🥗 Giảm cân"):
            st.session_state.goal = "Giảm cân"
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("💪 Tăng cơ"):
            st.session_state.goal = "Tăng cơ"
            st.session_state.step = 2
            st.rerun()
    with col3:
        if st.button("⚖️ Giữ dáng"):
            st.session_state.goal = "Giữ dáng"
            st.session_state.step = 2
            st.rerun()

# =======================
# SCREEN 2 – SLIDER DINH DƯỠNG
# =======================
elif st.session_state.step == 2:
    st.title("🍽️ Thiết kế bữa ăn")

    st.markdown("### Điều chỉnh dinh dưỡng")

    protein = st.slider("🥩 Protein (g)", 0, 100, 25)
    carb = st.slider("🍞 Carb (g)", 0, 100, 40)
    fat = st.slider("🧈 Fat (g)", 0, 50, 8)

    st.markdown("### Chọn dạng món")
    food_type = st.radio(
        "",
        ["🍜 Dạng sợi", "🥣 Dạng súp", "🥤 Dạng nước"]
    )

    st.markdown("### Chọn hương vị")
    flavor = st.radio(
        "",
        ["🐔 Gà tiêu", "🍄 Nấm", "🍫 Chocolate", "🍵 Matcha", "🧋 Trà sữa"]
    )

    if st.button("➡️ Tiếp tục"):
        st.session_state.meal = {
            "protein": protein,
            "carb": carb,
            "fat": fat,
            "type": food_type,
            "flavor": flavor
        }
        st.session_state.step = 3
        st.rerun()

# =======================
# SCREEN 3 – XÁC NHẬN
# =======================
elif st.session_state.step == 3:
    st.title("✅ Xác nhận bữa ăn")

    kcal = (
        st.session_state.meal["protein"] * 4 +
        st.session_state.meal["carb"] * 4 +
        st.session_state.meal["fat"] * 9
    )

    st.markdown(f"""
    ### 🧾 Thông tin dinh dưỡng
    - Protein: **{st.session_state.meal['protein']}g**
    - Carb: **{st.session_state.meal['carb']}g**
    - Fat: **{st.session_state.meal['fat']}g**
    - 🔥 **{kcal} kcal**
    """)

    if st.button("🚀 Send to NutriPod"):
        st.session_state.step = 4
        st.rerun()

# =======================
# SCREEN 4 – LOADING
# =======================
elif st.session_state.step == 4:
    st.title("🍳 Preparing your meal...")
    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.025)
        progress.progress(i + 1)

    st.session_state.step = 5
    st.rerun()

# =======================
# SCREEN 5 – HOÀN TẤT
# =======================
elif st.session_state.step == 5:
    st.title("✅ Meal Ready!")

    st.image(
        "https://images.unsplash.com/photo-1600891964599-f61ba0e24092",
        use_column_width=True
    )

    st.success("🍱 Bữa ăn của bạn đã sẵn sàng!")
    st.markdown("💡 *Remember: Đừng bỏ 4 capsule trà sữa 😆*")

    if st.button("🔁 Làm lại"):
        st.session_state.step = 1
        st.rerun()
