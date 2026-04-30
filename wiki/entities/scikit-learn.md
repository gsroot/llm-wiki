---
title: scikit-learn (sklearn)
aliases:
- scikit-learn
- 사이킷런
- sklearn
- 사이킷-런
type: entity
entity_type: tool
tags:
- scikit-learn
- sklearn
- machine-learning
- python
- classic-ml
- fit-predict-transform
- pipeline
- numfocus
- probabl
- slep
- agents-md
related:
- '[[microsoft-ml-for-beginners]]'
- '[[ml-ai]]'
- '[[data-pipeline-bigquery]]'
- '[[harness]]'
- '[[spec-driven-development]]'
- '[[scikit-learn-scikit-learn]]'
- '[[seokgeun-stack-guide]]'
- '[[microsoft-lightgbm]]'
source_count: 2
observed_source_refs: 30
inbound_count: 68
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 26
---

# scikit-learn (sklearn)

## 개요

Python에서 머신러닝의 사실상 표준(de facto) 라이브러리. 2007년 David Cournapeau가 Google Summer of Code 프로젝트로 시작, 2010-02-01 v0.1 첫 릴리스. 19년간 한 가지 API 컨트랙트(`fit`/`predict`/`transform`)를 지키며 입문자 교재부터 회사 BI까지 같은 코드 모양으로 작동시킨다는 점이 핵심 가치. **BSD 3-Clause** 라이선스로 상업 이용 자유. 2026-04-27 기준 GitHub ★65,932 / fork 26,974, 활발한 메인테넌스(오늘 push).

## 주요 특징

- **5가지 API 컨트랙트** — Estimator(`fit`) / Predictor(`predict`) / Transformer(`transform`) / Pipeline(`make_pipeline`) / Meta-estimator(`GridSearchCV` 류). 이 5개가 곧 라이브러리 전부의 추상화 모양.
- **+1 신규** (1.3+, experimental): **Metadata Routing API** — `set_fit_request(sample_weight=True)` 패턴, 19년의 "X, y만 다룬다" 컨트랙트 첫 명시적 확장.
- **의도적 범위 잠금**: 딥러닝/RL/그래픽 모델/시퀀스 예측/GPU "out of scope" 명시. 직사각형 데이터 위 정통 ML만.
- **거버넌스**: meritocratic + consensus seeking + **SLEP** (Scikit-Learn Enhancement Proposal, 별도 repo) 3중 강제. 4팀(Maintainers, Documentation, Contributor Experience, Communication) + Technical Committee 7명.
- **다층 자금 모델**: [[numfocus]] 재정 후원 / probabl.ai 풀타임 메인테이너 8명 고용 / Founding INRIA / Gold Chanel / Silver BNP Paribas / Bronze NVIDIA / Microsoft·Quansight·CZI·Tidelift 후원. 단일 회사 의존성 없음.
- **의존성 최소화**: Python 3.11+ / NumPy 1.24+ / SciPy 1.10+ / joblib 1.3+ / threadpoolctl 3.2+ — 5개만으로 작동.
- **빌드 시스템**: `pyproject.toml` + `meson.build` (Cython) — Python ML 라이브러리 중 드물게 meson 채택.
- **AGENTS.md** (965 bytes, 루트): 메이저 OSS 중 첫 명문화된 AI 작성 코드 disclosure 강제 정책.
- **인용**: Pedregosa et al. 2011 (JMLR) "scikit-learn: ML in Python" / Buitinck et al. 2013 "API design for ML software" / DOI `10.5281/zenodo.17880109` (학술 인용 가능 SW).

## API 컨트랙트 — 학습 곡선의 비밀

```
모든 객체 = BaseEstimator 상속
   ├── fit(X, y) -> self                  # Estimator (필수)
   │     X: (n_samples, n_features) array-like
   │     y: 1D array (regression: float / classification: int / unsup: 생략)
   ├── predict(X) -> y_pred               # Predictor (분류/회귀)
   ├── transform(X) -> X_new              # Transformer (전처리)
   ├── fit_transform(X, y=None)           # 둘 합친 단축
   ├── score(X, y) -> float               # 평가
   └── set_{method}_request(...)          # Metadata Routing (1.3+)
```

→ `Pipeline = Transformer1 → Transformer2 → ... → Predictor` (그 자체로 Estimator/Predictor 컨트랙트 만족)
→ `Meta-estimator(BaseEstimator)` (예: `GridSearchCV(estimator=RandomForestRegressor, ...)`)

이 모양 하나만 이해하면 60+ 알고리즘이 즉시 호환된다 — [[microsoft-ml-for-beginners]] 26 lesson이 같은 추상화로 회귀·분류·클러스터링·NLP·시계열을 다룰 수 있는 이유.

## 생태계 — 30개+ 호환 라이브러리

scikit-learn 컨트랙트를 따르면 자동 호환:

- **AutoML**: auto-sklearn, TPOT, MLJAR AutoML, EvalML, Featuretools, autoviml
- **실험 관리**: MLFlow, Neptune, Sacred, Scikit-Learn Laboratory
- **시각화·진단**: yellowbrick, dtreeviz, model-diagnostics
- **모델 배포**: sklearn-onnx, **skops.io** (안전 직렬화), sklearn2pmml, treelite, emlearn (마이크로컨트롤러)
- **가속**: Intel Extension for scikit-learn (메인테이너 미관여 명시)
- **R 인터페이스**: BiocSklearn (Bioconductor)

→ "라이브러리가 작은 [[harness]]" — sklearn 자체가 외부 호환 컴포넌트의 협업 표준 역할.

## 거버넌스 모델 — SLEP과 4가지 의사결정 룰

| 변경 종류 | 룰 |
|----------|------|
| 마이너 (오타 등) | lazy consensus: +1 by 1 core, no -1 |
| 코드 / 메이저 문서 | lazy consensus: +1 by 2 cores, no -1 |
| API 원칙 / 의존성 / 지원 버전 | **SLEP** + 1주+ 토론 + 2/3 다수결, 실패 시 TC |
| 거버넌스 자체 | SLEP020: PR 본문이 SLEP, 1개월 잠금, PR approval=+1, 2/3 통과 |

**Technical Committee** (현재 7명): Thomas Fan, Alexandre Gramfort, Olivier Grisel, Adrin Jalali, Andreas Müller, Joel Nothman, Gaël Varoquaux.

이 SLEP 모델은 [[github-spec-kit]] SDD나 [[anthropics-skills]] SKILL.md의 "표준화 → 구현" 분리 패턴의 19년 선배 사례.

## 모델 영속성 — 5단 의사결정 트리

`model_persistence.rst`의 의사결정 가이드 (이 위키에서 직접 BI 모델 배포 결정에 적용 가능):

1. Python 객체 필요? **No** → ONNX (가장 안전, 일부 모델만)
2. 모델 출처 신뢰? **No** → skops.io (보안 향상, 부분 검증)
3. 로딩 성능 중요? **Yes** → joblib (메모리 매핑 + 압축)
4. 표준 직렬화 실패? **Yes** → cloudpickle (호환성 보장 X)
5. 그 외 → 표준 직렬화

## 관련 개념

- [[ml-ai]]: 회사 BI에서 GCP AutoML / LangGraph 시대 — sklearn 직접 사용 시 비용 절감 + 코드 가시화
- [[data-pipeline-bigquery]]: BigQuery 데이터를 pandas로 추출 → sklearn Pipeline에 투입 패턴
- [[backend-python-fastapi]]: FastAPI로 sklearn 모델을 API화 (`fit`된 모델을 ONNX/joblib로 직렬화 후 서빙)
- [[harness]]: "라이브러리가 작은 하네스" 관점에서 sklearn은 5개 컨트랙트가 곧 작업 운영 패턴
- [[spec-driven-development]]: SLEP은 SDD의 19년 선배 — "메소드론을 별도 repo로 분리" 패턴
- [[agent-skills]]: AGENTS.md 패턴이 [[claude-code]] AGENTS.md와 같은 "에이전트 명세 표준화"
- [[microsoft-for-beginners]]: ML-For-Beginners가 sklearn API 컨트랙트만으로 26 lesson 작성

## 의사결정 컨텍스트 (raw 인용)

> "2007년 GSoC 프로젝트로 시작해 19년간 한 가지 API 컨트랙트(fit/predict/transform)를 지키며 Python 데이터 과학 스택의 '공식 베이스'로 자리잡은 라이브러리. 의도적으로 딥러닝/RL/구조적 학습을 회피하고 '직사각형 데이터 위의 정통 ML'에 범위를 잠근 결정 — 그 잠금이 microsoft-ml-for-beginners 입문 커리큘럼부터 c2spf-analytics BI 분석까지 모든 층의 표준 도구가 된 이유."
> — [[scikit-learn-scikit-learn]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 정통 ML 영역의 사실상 표준. [[c2spf-analytics|c2spf 게임 데이터 BI]] BI에서 유저 분석·세그멘테이션 후보 ([[lightgbm]]과 함께). [[pandas]] DataFrame 입력 + fit/predict/transform 컨트랙트가 [[ml-ai]] 카테고리 전체의 mental model. **19년 API 안정성**은 [[postgresql]] 30년 보수파와 함께 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 안정성 우선 거버넌스 사례. [[numfocus]] 후원.

## 출처

- [[scikit-learn-scikit-learn]] — 이 엔티티의 자체 소스 페이지 (메타·거버넌스·API·생태계 종합)
- [[microsoft-ml-for-beginners]] — sklearn 위에 만들어진 26 lesson 입문 커리큘럼
- [[microsoft-lightgbm]] — sklearn-compatible GBDT 라이브러리, Pipeline 1급 통합
- [[microsoft-lightgbm]] — sklearn-compatible GBDT 라이브러리, Pipeline 1급 통합

## sklearn vs LightGBM — 보완 관계

scikit-learn에는 자체 `GradientBoostingClassifier`/`HistGradientBoostingClassifier`가 있으나, 실무에서는 **[[lightgbm]]**이 GBDT 1순위. 이유와 통합 패턴:

| 축 | sklearn 내장 GBM | [[lightgbm]] |
|----|------------------|---------------|
| **속도** | 단일 스레드 기본 | Multi-threaded + GPU + 분산 |
| **메모리** | 보통 | Histogram-based + EFB로 절감 |
| **categorical** | 0.21+에서 부분 지원 | 1급 지원 (`category_feature`) |
| **API** | `BaseEstimator` 컨트랙트 | sklearn-compatible (`LGBMClassifier`) |
| **튜닝** | scikit-learn `GridSearchCV` | + Optuna LightGBM Tuner |

**통합 패턴**: LightGBM이 **sklearn 컨트랙트를 따르므로** Pipeline에 직접 삽입 가능. 즉 sklearn은 framework, LightGBM은 algorithm — 경쟁이 아닌 보완.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import lightgbm as lgb

pipe = Pipeline([
    ("scaler", StandardScaler),
    ("clf", lgb.LGBMClassifier(n_estimators=500, learning_rate=0.05)),
])
pipe.fit(X_train, y_train)  # sklearn 표준 컨트랙트 그대로
```

→ **5가지 API 컨트랙트의 19년 안정성**이 LightGBM·CatBoost·XGBoost 같은 외부 알고리즘이 1급으로 통합되는 이유.

## 메모

- **회사 BI 적용 후보**:
 1. 게임 사용자 이탈/구매 예측 — GCP AutoML Tables 대체로 sklearn `RandomForestClassifier` + `Pipeline(StandardScaler, ...)` 직접 사용 시 비용 절감 + 코드 가시화 + 모델 디버깅 가능.
 2. 시계열 (게임 매출/MAU) — sklearn에는 본격 시계열 도구 부족 → `make_regression` 기반 회귀 모델 + 외부 timeseries 라이브러리(statsmodels, prophet) 병용.
 3. A/B 테스트 가중치 — Metadata Routing API의 `sample_weight`로 신규/이탈 유저 가중치 다르게 학습.
- **개인 프로젝트 적용**:
 - 카카오톡 대화 분석 (Pandas + Plotly) → sklearn `KMeans` 클러스터링으로 대화 패턴 그룹화 추가 가능.
 - 트래블메이트 LangGraph 에이전트 → sklearn 분류기로 사용자 의도 보조 분류 가능 (LLM 부하 절감).
- **AGENTS.md 차용**: 사이드 프로젝트가 OSS 공개될 때 `AGENTS.md` 한 페이지에 disclosure + 코멘트 가이드만 박아도 큰 거버넌스 효과.
- **버전 잠금 위험**: sklearn 모델은 버전 간 직렬화 호환성 보장 안 함 — 프로덕션 배포 시 `pip freeze`로 정확한 버전 잠금 + validation set 예측 스냅샷 보관 (roadmap 17번 권장).
- **"3개월 릴리스 주기"**: 2010~ 약 3개월 주기로 새 버전 릴리스 — 회사 BI에서 의존성 업데이트 캘린더화 가능.
