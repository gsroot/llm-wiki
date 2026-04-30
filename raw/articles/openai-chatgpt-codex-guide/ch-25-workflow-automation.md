---
source_url: https://wikidocs.net/340837
book: ChatGPT & Codex 실무 활용 가이드
author: 송영옥
license: CC-BY (wikidocs by.png 아이콘 표시)
fetched_at: 2026-04-30
ingestion_mode: path-b-summary
---

# Chapter 25. 업무 자동화 워크플로 구축

## 페이지 구조 (헤딩 outline)
- 자동화 플랫폼 선택 가이드
- 노코드/로우코드 자동화 플랫폼 연동
  - Zapier + ChatGPT
  - Make(Integromat) + OpenAI 모듈
  - Microsoft Power Automate + AI Builder
- Slack 봇 만들기
  - Slack App 설정
  - Python Flask로 Slack 봇 구현
- Google Sheets / Notion 자동화
  - Google Apps Script + OpenAI API
- 실습: "이메일 수신 → AI 분류 → 자동 응답" 파이프라인 구축
  - 방식 1: Zapier 노코드 구현
  - 방식 2: Python 스크립트 구현
  - 두 방식 비교

## 핵심 요약 (자가 작문)

이 챕터는 ChatGPT API를 실제 업무 시스템에 꽂아 자동화 워크플로를 만드는 방법을 노코드와 코드 두 갈래로 정리한다. Zapier, Make(Integromat), Microsoft Power Automate 같은 노코드 플랫폼은 GUI로 트리거-액션을 묶어 빠르게 프로토타입을 만들기 좋고, Python·Flask·Google Apps Script 기반 코드 방식은 복잡한 분기 로직과 비용 효율 면에서 강점이 있다. 사례로 Slack 봇, Google Sheets 자동화, Notion 자동화가 단계별로 제시된다. 마지막 실습은 "이메일 수신 → AI 분류 → 자동 응답" 파이프라인을 Zapier와 Python 두 방식으로 각각 구현해 비교하는 형태다. 권장 패턴은 Zapier로 빠르게 검증하고, 사용량과 로직 복잡도가 늘어나면 Python으로 옮기는 단계적 전환이다.

## 인용 (key quotes, 짧게)

> "코드 없이 GUI로 연결하는 노코드/로우코드 플랫폼과, Python 스크립트로 직접 구현하는 코드 방식입니다."

> "간단한 파이프라인 시작은 Zapier로 빠르게 검증하고, 사용량이 늘거나 복잡한 로직이 필요해지면 Python으로 전환하는 전략이 효과적입니다."

## 메타 정보
- 표: 2개 / 코드블록: 4개 / 이미지: 0개
- 마지막 편집: 2026-04-12

원본: https://wikidocs.net/340837
