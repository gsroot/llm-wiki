---
source_url: https://wikidocs.net/340835
book: ChatGPT & Codex 실무 활용 가이드
author: 송영옥
license: CC-BY (wikidocs by.png 아이콘 표시)
fetched_at: 2026-04-30
ingestion_mode: path-b-summary
---

# Chapter 23. OpenAI API 시작하기

## 페이지 구조 (헤딩 outline)
- OpenAI API란?
- API 키 발급하기
  - 1단계: 계정 생성
  - 2단계: API 키 생성
  - 3단계: 결제 수단 등록
- 개발 환경 설정
  - Python 환경
  - JavaScript / Node.js 환경
- 첫 번째 API 호출
- Chat Completions API 구조 이해
  - messages 배열과 역할(role)
  - 주요 파라미터
  - 응답 구조
- 모델 선택 가이드
- 비용 관리
  - 토큰 개념
  - 비용 절감 전략
  - Rate Limit 이해와 대응
- 실습: 이메일 자동 분류기 만들기

## 핵심 요약 (자가 작문)

이 챕터는 OpenAI API를 처음 다루는 독자를 위한 출발점이다. 계정 생성, API 키 발급, 결제 수단 등록을 거쳐 Python·Node.js 개발 환경을 세팅하고 첫 호출을 만들어 보는 흐름으로 진행된다. 이어 Chat Completions API의 messages 배열 구조와 system/user/assistant 역할, temperature·max_tokens 같은 파라미터, 응답 JSON 구조를 단계적으로 설명한다. 모델 선택 가이드에서는 일반 업무 자동화에 gpt-4o-mini가 비용·속도 면에서 가장 효율적이라는 가이드라인이 제시되고, 토큰 기반 과금과 rate limit 대응 전략도 함께 다뤄진다. 보안 관점에서 API 키는 비밀번호와 동급으로 취급해 환경 변수로만 관리해야 한다는 점이 반복 강조된다. 실습은 이메일 자동 분류기 구현으로 마무리.

## 인용 (key quotes, 짧게)

> "API 키는 비밀번호와 같습니다. 코드에 직접 입력하지 말고 반드시 환경 변수나 별도의 설정 파일로 관리하세요."

> "일반적인 업무 자동화에는 gpt-4o-mini가 속도와 비용 면에서 가장 효율적입니다."

## 메타 정보
- 표: 4개 / 코드블록: 10개 이상 / 이미지: 1개
- 마지막 편집: 2026-04-12

원본: https://wikidocs.net/340835
