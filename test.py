import streamlit as st
import urllib.request

# MBTI별 추천 직업 및 포켓몬 데이터
# 포켓몬 이미지는 영문 이름을 기반으로 두 개의 이미지 소스(pokemondb, PokeAPI)를
# 순서대로 시도해서 하나라도 로드되면 표시합니다.
MBTI_DATA = {
    "INTJ": {"job": "전략 컨설턴트 / 데이터 과학자", "pokemon": "슈퍼땅콩(알라카잠)", "name_en": "alakazam", "id": 65,
              "reason": "치밀한 분석력과 미래를 내다보는 통찰력이 닮았어요."},
    "INTP": {"job": "연구원 / 소프트웨어 엔지니어", "pokemon": "폴리곤", "name_en": "porygon", "id": 137,
              "reason": "논리적 사고와 새로운 원리를 탐구하는 호기심이 잘 맞아요."},
    "ENTJ": {"job": "경영자 / 프로젝트 매니저", "pokemon": "리자몽", "name_en": "charizard", "id": 6,
              "reason": "강한 추진력과 카리스마 있는 리더십이 닮았어요."},
    "ENTP": {"job": "스타트업 창업가 / 마케터", "pokemon": "조로아크", "name_en": "zoroark", "id": 571,
              "reason": "재치와 기발한 발상, 임기응변 능력이 잘 어울려요."},
    "INFJ": {"job": "상담가 / 심리치료사", "pokemon": "뮤", "name_en": "mew", "id": 151,
              "reason": "깊은 통찰력과 타인을 이해하는 따뜻함이 닮았어요."},
    "INFP": {"job": "작가 / 예술가", "pokemon": "가디안", "name_en": "gardevoir", "id": 282,
              "reason": "섬세한 감수성과 이상을 추구하는 마음이 잘 맞아요."},
    "ENFJ": {"job": "교육자 / 코치", "pokemon": "루카리오", "name_en": "lucario", "id": 448,
              "reason": "타인의 성장을 돕는 리더십과 신념이 닮았어요."},
    "ENFP": {"job": "크리에이터 / 마케터", "pokemon": "이브이", "name_en": "eevee", "id": 133,
              "reason": "무한한 가능성과 자유로운 에너지가 잘 어울려요."},
    "ISTJ": {"job": "회계사 / 공무원", "pokemon": "메탕그로스", "name_en": "metagross", "id": 376,
              "reason": "꼼꼼함과 책임감, 원칙을 지키는 성실함이 닮았어요."},
    "ISFJ": {"job": "간호사 / 사회복지사", "pokemon": "럭키", "name_en": "chansey", "id": 113,
              "reason": "따뜻한 보살핌과 헌신적인 성격이 잘 맞아요."},
    "ESTJ": {"job": "관리자 / 군인", "pokemon": "괴력몬", "name_en": "machamp", "id": 68,
              "reason": "체계적인 실행력과 강한 책임감이 닮았어요."},
    "ESFJ": {"job": "이벤트 기획자 / 교사", "pokemon": "푸크린", "name_en": "wigglytuff", "id": 40,
              "reason": "사교성과 주변을 챙기는 배려심이 잘 어울려요."},
    "ISTP": {"job": "엔지니어 / 정비사", "pokemon": "핫삼", "name_en": "scizor", "id": 212,
              "reason": "냉철한 문제 해결 능력과 실용성이 닮았어요."},
    "ISFP": {"job": "디자이너 / 사진작가", "pokemon": "샤미드", "name_en": "vaporeon", "id": 134,
              "reason": "유연한 감각과 자유로운 예술적 성향이 잘 맞아요."},
    "ESTP": {"job": "영업 전문가 / 기업가", "pokemon": "번치코", "name_en": "blaziken", "id": 257,
              "reason": "과감한 실행력과 승부욕이 닮았어요."},
    "ESFP": {"job": "배우 / 엔터테이너", "pokemon": "피카츄", "name_en": "pikachu", "id": 25,
              "reason": "밝은 에너지와 사람들을 즐겁게 하는 매력이 잘 어울려요."},
}


def get_image_candidates(name_en: str, dex_id: int):
    """이미지 소스 후보 URL 목록을 반환합니다. 하나가 실패하면 다음 것을 시도합니다."""
    return [
        f"https://img.pokemondb.net/artwork/large/{name_en}.png",
        f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dex_id}.png",
        f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{dex_id}.png",
    ]


@st.cache_data(show_spinner=False)
def fetch_image_bytes(url: str):
    """서버에서 직접 이미지를 다운로드합니다. 브라우저가 URL을 못 불러오는 문제를 우회합니다."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=5) as response:
        return response.read()

st.set_page_config(page_title="MBTI 직업 & 포켓몬 추천", page_icon="✨", layout="centered")

st.title("✨ MBTI 직업 & 포켓몬 추천기")
st.write("MBTI를 선택하면 어울리는 직업과 포켓몬을 추천해드려요!")

mbti_list = list(MBTI_DATA.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("추천 받기"):
    data = MBTI_DATA[selected_mbti]
    st.subheader(f"🧑‍💼 추천 직업: {data['job']}")
    st.subheader(f"⚡ 추천 포켓몬: {data['pokemon']}")

    candidates = get_image_candidates(data["name_en"], data["id"])
    shown = False
    for url in candidates:
        try:
            img_bytes = fetch_image_bytes(url)
            st.image(img_bytes, caption=data["pokemon"], width=300)
            shown = True
            break
        except Exception:
            continue

    if not shown:
        st.warning("이미지를 불러오지 못했어요. 아래 링크에서 확인해주세요.")
        st.markdown(f"[포켓몬 이미지 보기]({candidates[0]})")

    st.info(f"💡 추천 이유: {data['reason']}")

st.markdown("---")
st.caption("Made with Streamlit ⚡ Pokemon 이미지 출처: PokeAPI")
