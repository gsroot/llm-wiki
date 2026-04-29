---
title: "Google"
type: entity
entity_type: organization
tags: [google, alphabet, big-tech, gemini, antigravity, flutter, dart, android, chrome, skia, deepmind, cloud, devrel, AI]
related:
  - "[[flutter]]"
  - "[[dart]]"
  - "[[github]]"
  - "[[microsoft]]"
  - "[[anthropic]]"
source_count: 1
created: 2026-04-27
updated: 2026-04-27
---

# Google

## 개요

**Google** (모회사 Alphabet, 1998년 설립)은 검색·광고·클라우드·AI·OS·브라우저·하드웨어 등 IT 산업 전 영역에 걸친 빅테크다. 위키 관점에서 Google이 중요한 이유는 (1) [[flutter]] + [[dart]]를 11년간 주도해 온 멀티플랫폼 UI SDK 공급자, (2) **Gemini** 모델·**Antigravity** AI IDE·**Gemini Code Assist**로 [[anthropic]] Claude 진영과 직접 경쟁, (3) Skia·Android 등의 인프라가 다른 진영(Flutter, Chrome OS 등)에서도 기반으로 사용된다는 점.

[[microsoft]] (개발자 교육 + Copilot 통합)·[[anthropic]] (모델 + agent-skills 표준)와 함께 **AI 코딩 도구 시장 3대 진영** 중 하나. Google의 차별점: 하드웨어(Pixel)·OS(Android, ChromeOS)·브라우저(Chrome)·클라우드(GCP)·개발 도구(Flutter, Dart, Antigravity)를 수직 통합으로 보유.

## 주요 특징

### 위키 관련 핵심 자산

| 자산 | 위키 관련성 |
|------|-----------|
| **[[flutter]]** | 멀티플랫폼 UI SDK — 11년차 ★176K OSS, agent-skills 표준 채택 |
| **[[dart]]** | Flutter의 framework 언어, 4-target compile |
| **Gemini** | LLM 모델 패밀리 (Pro/Flash/Ultra). 1M+ 토큰 컨텍스트 |
| **Gemini Code Assist** | IDE 통합 AI 코딩 도구. flutter/flutter 저장소가 `.gemini/styleguide.md`로 직접 통합 |
| **Antigravity** | AI IDE — 룰 한계 12,000자 hard limit ([[flutter]] `docs/rules/rules_10k.md`가 대응) |
| **Skia** | 2D 그래픽 라이브러리. [[flutter]] + Chrome + Android의 공통 기반 |
| **Android** | 모바일 OS. Flutter의 주요 deploy 타깃 중 하나 |
| **Chrome / V8** | 브라우저. JavaScript 엔진 V8이 Dart VM 설계에 영향 |
| **Google Cloud** | GCP, BigQuery (석근의 [[c2spf-analytics]] 핵심 인프라), Vertex AI |

### AI 진영 위치

| 차원 | 입장 |
|------|------|
| **모델** | Gemini Pro/Flash/Ultra (1M+ 토큰 컨텍스트가 차별점) |
| **agent-skills 표준** | flutter/flutter `.agents/skills/`로 외부 채택 (위치는 vendor-neutral) |
| **AI IDE** | Antigravity (룰 12K hard limit), Gemini Code Assist (`.gemini/` 통합) |
| **에이전트 SDK** | Gemini API + Vertex AI Agent Builder |
| **MCP** | 공식 MCP 서버 보유 (BigQuery 등) |

### 거버넌스 모델

- **Flutter Team**: Google 내부 팀이 stewardship 보유, 그러나 majority committers는 외부
- **OSS 비중**: Android, Chromium, Skia, Flutter, Dart, Tensorflow 등 대규모 OSS 다수 — 인프라 OSS는 거의 다 Google 출신
- **DevRel**: Cloud Advocates 모델은 [[microsoft]]가 더 발달, Google은 Codelabs·I/O 컨퍼런스 중심

## 관련 개념

- [[flutter]]: Google의 대표 OSS framework — 멀티플랫폼 UI SDK
- [[dart]]: Flutter의 단독 framework 언어
- [[github]]: Microsoft 자회사이지만 Google의 OSS(Flutter, Dart, Skia 등) 호스팅 — 빅테크 간 인프라 의존
- [[microsoft]]: AI 진영 경쟁자 (Copilot vs Gemini Code Assist), 그러나 Microsoft for-beginners 커리큘럼은 Google 도구도 다룸
- [[anthropic]]: AI 진영 경쟁자 (Claude vs Gemini). agent-skills 표준은 Anthropic 정의, Google 사용 자산은 그 표준 채택

## 출처

- [[flutter-flutter]] — Flutter SDK의 모기관으로 등장. README "Google's SDK" 표제 + `docs/about/Values.md`의 "Flutter's stewardship is managed by a team at Google" + `.gemini/` 디렉토리 통합 + `docs/rules/README.md`의 도구별 한계 매트릭스에서 Antigravity·Gemini CLI 한계 명시

## 메모

- 위키 진영 분류상 Google은 [[microsoft]]·[[anthropic]]·[[github]]와 동격 organization. 향후 Google 단일 자료(예: Vertex AI 문서, BigQuery 문서, Gemini API 문서, AI Studio) 수집 시 본 페이지에 collation
- 석근의 회사 BI([[c2spf-analytics]])가 Google Cloud BigQuery에 의존 — Google과의 직접 접점. 그러나 위키 단계에서는 BigQuery를 별도 도구로 등록 ([[data-pipeline-bigquery]] 개념 페이지가 이미 존재)
- 후속 탐구: (a) Google의 AI 도구 스택(Gemini Code Assist, Antigravity, Vertex AI Agent Builder, NotebookLM) 종합 비교, (b) [[microsoft]]·[[anthropic]] 페이지와의 균형 점검 — Google이 organization 페이지 신설된 첫 회차이므로 후속 자료 누적 필요
