---
title: "Obsidian Web Clipper"
type: entity
entity_type: tool
tags: [obsidian, 웹클리핑, web-clipper, 소스수집, 마크다운, markdown]
related:
  - "[[obsidian]]"
  - "[[llm-wiki-pattern]]"
source_count: 1
created: 2026-04-09
updated: 2026-04-09
---

# Obsidian Web Clipper

## 개요

웹 기사를 마크다운으로 변환하는 브라우저 확장 프로그램. LLM 위키에서 `raw/articles/`에 웹 소스를 빠르게 가져오는 1차 수집 도구로 활용된다.

## 주요 특징

- 웹 페이지를 깔끔한 마크다운으로 변환
- Obsidian 볼트의 지정 폴더에 직접 저장 가능
- 프론트매터(제목, URL, 날짜 등) 자동 생성
- 이미지는 기본적으로 URL 참조로 저장됨

## 이미지 로컬 다운로드 팁

원문 소스에서 제안하는 이미지 로컬화 워크플로우:

1. Obsidian 설정 → 파일 및 링크 → 첨부 파일 폴더 경로를 `raw/assets/`로 설정
2. 설정 → 단축키에서 "Download attachments for current file" 검색
3. 단축키 바인딩 (예: Ctrl+Shift+D)
4. 기사 클리핑 후 단축키로 이미지 일괄 로컬 다운로드

이렇게 하면 LLM이 깨질 수 있는 URL에 의존하지 않고 이미지를 직접 참조할 수 있다.

## 관련 개념

- [[obsidian]]: Obsidian 본체. 이 확장은 Obsidian vault의 지정 폴더로 클리핑을 직접 저장
- [[llm-wiki-pattern]]: 수집(Ingest) 워크플로우의 소스 획득 단계에서 핵심 도구

## 출처

- [[llm-wiki-idea-doc]] — 팁과 요령 섹션 및 역자 주석 5번에서 소개

## 메모

- Web Clipper 외에도 다양한 소스 수집 경로가 있다:
  - YouTube 자막: `yt-dlp --write-auto-sub`
  - PDF 논문: `marker`로 마크다운 변환
  - 트위터 스레드: Thread Reader App → Web Clipper
  - 팟캐스트: Whisper로 트랜스크립트 생성
- 소스마다 메타데이터(날짜, 저자, URL, 유형)를 프론트매터로 통일하면 Dataview 활용도가 높아진다.
