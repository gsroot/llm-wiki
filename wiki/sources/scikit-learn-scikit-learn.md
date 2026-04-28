---
title: "scikit-learn/scikit-learn — Python 머신러닝의 사실상 표준 라이브러리 (BSD-3, 2007~)"
type: source
source_type: article
source_url: "https://github.com/scikit-learn/scikit-learn"
raw_path: "raw/articles/scikit-learn-scikit-learn/"
author: "scikit-learn community (David Cournapeau 시작 / INRIA 인큐베이션 / NumFOCUS 재정 후원 / probabl.ai 풀타임 메인테이너 고용)"
date_published: 2010-02-01
date_ingested: 2026-04-27
tags: [scikit-learn, sklearn, machine-learning, python, classic-ml, fit-predict-transform, pipeline, estimator-api, slep, governance, numfocus, probabl, agents-md, ai-disclosure]
related:
  - "[[microsoft-ml-for-beginners]]"
  - "[[ml-ai]]"
  - "[[data-pipeline-bigquery]]"
  - "[[com2us-platform]]"
confidence: high
---

# scikit-learn/scikit-learn — Python 머신러닝의 사실상 표준 라이브러리 (BSD-3, 2007~)

## 한줄 요약

> 2007년 GSoC 프로젝트로 시작해 19년간 한 가지 API 컨트랙트(`fit`/`predict`/`transform`)를 지키며 Python 데이터 과학 스택의 "공식 베이스"로 자리잡은 라이브러리. 의도적으로 딥러닝/RL/구조적 학습을 회피하고 "직사각형 데이터(rectangular data) 위의 정통 ML"에 범위를 잠근 결정 — 그리고 그 잠금이 [[microsoft-ml-for-beginners]] 같은 입문 커리큘럼부터 [[c2spf-analytics]] BI 분석까지 모든 층의 표준 도구가 된 이유.

## 메타

- 라이선스: **BSD 3-Clause** ("New" / "Revised") — `scikits.learn` → `scikit-learn` 개명, INRIA가 일부 코드 저작권 보유
- 별 **65,932** / fork **26,974** / open issues **2,048** / watchers·subscribers **2,119** (2026-04-27 기준)
- 첫 GitHub commit 2010-08-17 — 2010-02-01 v0.1 첫 공개 릴리스 / 약 3개월 주기 릴리스
- DOI: `10.5281/zenodo.17880109` — 학술 인용 가능한 SW
- 의존성 최소 셋: Python 3.11+ / NumPy 1.24+ / SciPy 1.10+ / joblib 1.3+ / threadpoolctl 3.2+
- 선택 의존성: matplotlib(시각화), pandas(데이터), seaborn/plotly(예제), scikit-image(이미지 예제), pytest(테스트)
- 빌드: `pyproject.toml` + **meson.build** (Cython 컴파일) — Python ML 라이브러리에선 드물게 meson 채택
- 코드 스타일: **ruff** (`.pre-commit-config.yaml`) — 2024~ 도입, black + flake8 단계 폐기
- 인용 논문 둘: Pedregosa et al. 2011 (JMLR) "scikit-learn: ML in Python" / Buitinck et al. 2013 (ECML PKDD) "API design for ML software"

## 거버넌스 — meritocratic + consensus seeking + SLEP

세 단계 권한:

1. **Contributors** — 한 번 기여하면 자동으로 기여자 (투표권 없음)
2. **Core Contributors** (4 팀) — 투표권 있음, 1년 비활성 시 emeritus 권유 메일
   - **Maintainers Team** — PR 머지·API 결정 (현재 19명, 풀타임 8명은 probabl.ai 고용)
   - **Documentation Team** — 문서 PR 권위 머지권
   - **Contributor Experience Team** — 이슈/PR 트리아지
   - **Communication Team** — SNS·블로그·브랜딩 (블로그 별도 repo, scikit-learn은 7개 SNS 채널 운영: TikTok·Bluesky·Mastodon·LinkedIn 포함)
3. **Technical Committee** (7명) — Thomas Fan, Alexandre Gramfort, Olivier Grisel, Adrin Jalali, Andreas Müller, Joel Nothman, Gaël Varoquaux — 컨센서스 실패 시 최종 결정자

**의사결정 룰** (4가지):
- **마이너 변경**: lazy consensus (+1 by 1 core, no -1)
- **코드 / 메이저 문서 변경**: lazy consensus (+1 by 2 cores, no -1)
- **API 원칙 / 의존성 / 지원 버전**: SLEP 필수 — 최소 1주 공개 토론 후 투표, 2/3 다수결, 실패 시 TC로 escalate
- **거버넌스 변경**: SLEP020 정의 — PR 본문이 SLEP, 1개월 투표 기간 잠금, PR approval = +1 / Request Changes = -1, 2/3 통과

**SLEP** (Scikit-Learn Enhancement Proposal) — `scikit-learn-enhancement-proposals` 별도 repo의 SLEP000 정의. PEP 모델 차용. 코드 변경에 메소드론적 사전 합성을 강제 — [[github-spec-kit]]의 SDD나 [[anthropics-skills]]의 SKILL.md와 같은 "표준화 → 구현" 분리 패턴이지만 19년 먼저 안착됨.

## 자금 모델 — multi-funder community

[[numfocus|NumFOCUS]](501c3) 재정 후원 + 다층 스폰서:

- **probabl.ai** — 스폰서십 프로그램 운영 + 풀타임 메인테이너 8명 고용 (Adrin Jalali, Olivier Grisel 등)
- Founding sponsor: **INRIA** (창립부터)
- Gold: Chanel / Silver: BNP Paribas / Bronze: NVIDIA (Tim Head 풀타임 고용)
- Other: Microsoft (Andreas Müller 2020~), Quansight Labs, Chan-Zuckerberg Initiative + Wellcome Trust (EOSS cycle 6), Tidelift
- Donations in kind: Anaconda(스토리지), CircleCI(CPU), GitHub(CPU + Teams)
- 50회+ coding sprint (2010~) — 오프라인 협업 모델

석근 시점 시사점: **회사가 PyTorch처럼 단일 기업이 만든 게 아니라 다층 스폰서가 떠받친다는 점**이 19년 안정성의 비밀. AutoML/LangGraph 등 단일 회사 도구와 차원이 다른 위험 분산.

## 핵심 API 설계 — 19년간 변하지 않은 5가지 컨트랙트

1. **Estimator** = `fit(X, y) -> self` 컨트랙트 인터페이스. `BaseEstimator` 상속.
   - `X`: `(n_samples, n_features)` 2D array-like
   - `y`: 1D array (regression: float / classification: int / unsupervised: 생략)
2. **Predictor** = Estimator + `predict(X) -> y_pred` (분류기·회귀기)
3. **Transformer** = Estimator + `transform(X) -> X_new` (`StandardScaler`, `ColumnTransformer` 등)
4. **Pipeline** = `make_pipeline(Transformer1, Transformer2, ..., Predictor)` — 그 자체로 Estimator·Predictor 컨트랙트 만족 → "데이터 누출(data leakage) 방지"의 일차 수단
5. **Meta-estimator** = Estimator를 인자로 받는 Estimator (`GridSearchCV`, `RandomizedSearchCV`, `BaggingClassifier` 등) → 하이퍼파라미터 자동 탐색·앙상블의 통일된 패턴

이 5개가 곧 [[microsoft-ml-for-beginners]]가 26 lesson 동안 처음부터 끝까지 그대로 쓰는 추상화 — "한 번 배우면 모든 sklearn 코드가 같은 모양"이 입문자의 진입 장벽을 깬 진짜 이유.

**최근 추가된 6번째 컨트랙트 (1.3+, 2023~)**: **Metadata Routing API** — `set_fit_request(sample_weight=True)` 같은 `set_{method}_request()` 패턴으로 `sample_weight`·`groups` 같은 메타데이터를 meta-estimator를 통과해 라우팅. 19년의 "X, y만 다룬다" 컨트랙트의 첫 명시적 확장 — 아직 experimental, `sklearn.set_config(enable_metadata_routing=True)`로 옵트인. 2018 로드맵 항목 5·6번 ("Passing around information that is not (X, y)")의 9년 후 부분 답.

## 의도적 범위 잠금 — "안 한다"의 명시화

FAQ는 "Why not deep learning / RL / graphical models / sequence prediction / GPU?" 질문에 일관되게 **"out of scope"**로 답함:

- **딥러닝·RL** → "different design constraints, GPU 필요" → tensorflow/keras/pytorch 추천. 단 `sklearn.neural_network`의 단순 MLP는 **버그 픽스만** 수용.
- **그래픽 모델·시퀀스 예측** → "redesign the whole package, project would collapse"
- **GPU** → 메인 라이브러리는 CPU only. Intel(R) Extension(`scikit-learn-intelex`) 같은 제3자 가속기는 **별도 프로젝트로 분리** (sklearn 메인테이너 미관여 명시)

**범위 잠금이 곧 신뢰**: "scikit-learn은 직사각형 데이터의 정통 ML만 한다"는 19년 약속이 외부 호환 라이브러리 생태계(scikit-learn-contrib, sklearn-onnx, skops, treelite, emlearn, yellowbrick, dtreeviz, MLFlow, auto-sklearn, TPOT 등 30개+)를 가능케 함. [[harness]] 관점에서는 **"라이브러리 자체가 작은 하네스"**의 사례.

## 2018 Roadmap — 9년 후에도 유효한 이슈들

2018에 발표된 18개 항목 중 일부는 여전히 미해결:

- 1번 Pandas DataFrame 핸들링 → `set_output(transform="pandas")` (1.2+)로 부분 해결
- 2번 Categorical features → `HistGradientBoostingClassifier` 네이티브 지원 (1.0+) / 트리 기반은 issue #29437 (진행 중)
- 6번 X, y 외 정보 전달 → Metadata Routing API (1.3+, 2023)로 부분 해결
- 14번 Distributed parallelism → `__array_function__` 호환 / Array API standard로 진행
- 16번 Backwards-compatible 직렬화 → `skops.io` 별도 라이브러리로 위임
- 17번 Model lifecycle 관리 → `model_persistence.rst`에 ONNX/skops/joblib/직렬화 5가지 비교표로 가이드화

**시사점**: 19년 운영 끝에도 "ideal API"는 도달 못 한 상태 — 그래서 SLEP 절차로 변경 강제. [[spec-driven-development]]가 "executable specification"을 강조하지만, scikit-learn은 **테스트 스위트(`pytest sklearn`) + 공통 테스트 헬퍼 + SLEP**의 3중 강제로 같은 결과 달성.

## 모델 영속성 — 5가지 옵션 비교

`model_persistence.rst`에 의사결정 트리:

| 방법 | 장점 | 단점 |
|------|------|------|
| **ONNX** | Python 환경 불필요, 가장 안전 | 일부 모델만 지원, 커스텀 estimator 어려움, Python 객체 복원 불가 |
| **skops.io** | 보안 향상, 부분 검증 가능 | 직렬화 속도 느림, 적은 타입, 같은 환경 필요 |
| **표준 직렬화** | Python 네이티브, 거의 모든 객체 | 임의 코드 실행 위험, 같은 환경 필요 |
| **joblib** | 메모리 매핑, 압축 단축 | 직렬화 기반 동일 위험 |
| **cloudpickle** | non-packaged 코드 직렬화 | 호환성 보장 없음, 기반 동일 위험 |

**4가지 의사결정 질문**:
1. Python 객체 필요? → No → ONNX
2. 모델 출처 신뢰? → No → skops.io
3. 로딩 성능 중요? → Yes → joblib
4. 표준 직렬화 실패? → cloudpickle

이 5단 비교표는 곧 **"어떤 ML 모델 직렬화 결정이든 5분 안에 답이 나오는 경량 의사결정 도구"** — 회사 BI에서 모델을 프로덕션으로 옮길 때 그대로 사용 가능.

## AGENTS.md — 메이저 OSS의 AI 거버넌스 첫 사례

루트의 `AGENTS.md`는 짧지만 (965 bytes) 강력하다:

> **REQUIRED: AI/Agent Disclosure** — Every summary, pull request description, or work description **MUST** include this disclosure:
> "This pull request includes code written with the assistance of AI. The code has not yet been reviewed by a human."
> This is a **mandatory requirement**, not optional.

추가로 "Generated Summaries" 섹션에서:
- "describe the why, highlight areas requiring careful review"
- "**Reduce the verbosity of your comments** — avoid flattery, avoid stating the obvious, avoid filler phrases, prefer technical clarity over marketing tone"

**메이저 OSS 프로젝트의 AI 통합 정책 첫 명문화 사례**. [[claude-code]], [[github-spec-kit]] 같은 에이전트 도구가 한쪽에서 제작 효율을 높이고, scikit-learn 같은 OSS는 반대편에서 disclosure를 강제 — **에이전트 시대의 두 축이 PR 한 페이지에서 만나는 지점**.

## 학습 리소스

- 공식: https://scikit-learn.org (안정 / dev 분리)
- 블로그: https://blog.scikit-learn.org (별도 repo, Communication Team 운영)
- 메일링: scikit-learn@python.org (Python 공식 메일)
- Discord: https://discord.gg/h9qyrK8Jc8 / GitHub Discussions / Stack Overflow `scikit-learn` 태그
- 7개 SNS: LinkedIn, YouTube, Facebook, Instagram, TikTok, Bluesky, Mastodon (fosstodon.org)
- 캘린더: https://blog.scikit-learn.org/calendar/ (스프린트 일정)

**SNS 7개 운영**은 19년 OSS 중 드문 디지털 마케팅 깊이 — Communication Team이 별도 권한·repo 갖는 거버넌스의 성과.

## 석근에게 가장 가치있는 부분

1. **`fit/predict/transform/pipeline` 5개 컨트랙트** — 회사 BI에서 사용자 이탈/구매 예측 모델 ([[ml-ai]] AutoML 시대) 재구현 시 sklearn 직접 사용으로 GCP AutoML 비용 절감 + 코드 가시화 가능
2. **`model_persistence.rst` 5단 의사결정 트리** — 회사 BI 모델 프로덕션 이동 시 그대로 적용 (현재 GCP AI Platform Pipeline 의존도 → 자체 sklearn + ONNX/joblib 옵션 평가 가능)
3. **Metadata Routing API** — `sample_weight`로 신규/이탈 유저 가중치 다르게 학습 (BI에서 흔한 시나리오)
4. **거버넌스 모델** — 위키 자체에 "SLEP-style" 메타 변경 절차 차용 가능 (CLAUDE.md를 위키의 SLEP000으로, 큰 구조 변경은 PR 토론 후 머지)
5. **AGENTS.md 패턴** — 사이드 프로젝트가 OSS화될 때 AI disclosure 정책 차용 (트래블메이트, Mate Chat 등이 OSS 공개되면)
6. **scikit-learn-contrib + skops + sklearn-onnx 생태계** — 회사 BI 모델을 외부 도구로 확장할 때 어떤 보조 라이브러리를 어느 단계에서 도입할지 결정 가이드

## 관련 엔티티/개념

- [[scikit-learn]] (entity, 신규) — 도구 정보 정리
- [[microsoft-ml-for-beginners]] — 26 lesson이 이 라이브러리만 사용
- [[ml-ai]] — 회사 AutoML 시대와 scikit-learn 직접 사용 비교 가능
- [[data-pipeline-bigquery]] — BigQuery에서 추출한 데이터를 sklearn 파이프라인에 넣는 패턴
- [[backend-python-fastapi]] — FastAPI로 sklearn 모델을 API화
- [[harness]] — "라이브러리가 작은 하네스" 사례, 5개 컨트랙트가 곧 작업 운영 패턴
- [[spec-driven-development]] — SLEP은 SDD의 19년 선배

## 인용

> "scikit-learn remains very popular in practice for trying out canonical machine learning techniques, particularly for applications in experimental science and in data science. A lot of what we provide is now very mature. But it can be costly to maintain, and we cannot therefore include arbitrary new implementations. Yet Scikit-learn is also essential in defining an API framework for the development of interoperable machine learning components external to the core library."
> — `doc/roadmap.rst`, Statement of purpose: Scikit-learn in 2018

> "It is currently maintained by a team of volunteers."
> — `README.rst` (자금 후원이 다층이지만, 의사결정은 여전히 자원봉사자 컨센서스)

## 메모

- **수집 선별**: `sklearn/` 핵심 코드는 raw에 보관하지 않음 — 메소드론·거버넌스·API 설계 철학은 모두 마크다운/RST에 박혀있고, 실제 코드는 GitHub 그대로 참조하면 됨. ([[github-spec-kit]] 수집과 동일 원칙)
- **org=repo 첫 사례**: `scikit-learn/scikit-learn` — `pandas-dev/pandas` (org≠repo) 컨벤션의 자연스러운 확장. raw 경로 `raw/articles/scikit-learn-scikit-learn/`로 일관성 유지.
- **다음 단계**:
  1. `glossary.rst` (94KB)는 보관하지 않음 — 너무 큼, 위키링크로 충분. 필요 시 `https://scikit-learn.org/stable/glossary.html` 직접 참조.
  2. **공통 테스트 헬퍼** (`sklearn/utils/estimator_checks.py`)는 sklearn 커스텀 estimator 작성 시 핵심 — 별도 후속 탐구 후보.
  3. SLEP 별도 repo (`scikit-learn-enhancement-proposals`) 수집 — SLEP020 (governance) / SLEP000 (process) 정도면 위키에서 "표준화 패턴 모음"으로 [[github-spec-kit]] / [[anthropics-skills]]과 4축 비교 종합 분석 가능.
- **자기 차용 분석**: 위키의 운영 절차 변경(예: lint 자동화, 새 카테고리 추가)을 SLEP-style로 다룬다면 — 단발 PR이 아닌 메타 변경은 명시적 토론 + 잠금 기간 + 머지 룰. 위키 100 페이지 후로 미루기.
