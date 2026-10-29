import streamlit as st

st.title("🤖 미술 큐레이터 페르소나 챗봇")
st.write("특정 역할을 수행하는 AI 챗봇 서비스입니다.")

# 세션 상태에 대화 기록이 없으면 초기화
if "messages" not in st.session_state:
  st.session_state.messages = [{
      "role": "assistant",
      "content": (
          "안녕하세요! 저는 전문 미술 큐레이터입니다. 작품이나 전시회에 대해"
          " 무엇이든 물어보세요!"
      ),
  }]

# 이전 대화 화면에 출력하기
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# 사용자 입력 받기
if prompt := st.chat_input("질문을 입력해주세요..."):
  # 사용자 메시지 추가 및 출력
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # 챗봇 응답 생성 (추후 LLM API 연동 코드로 대체 가능)
  with st.chat_message("assistant"):
    response = (
        f"'{prompt}'에 대해 큐레이터로서 멋진 예술적 해석을 제공해 드릴게요!"
    )
    st.markdown(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
