---
source_url: https://wikidocs.net/340839
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## Chapter 26. ChatGPT Team & Enterprise 도입

개인 계정으로 ChatGPT를 사용하다 보면 한계를 느끼는 순간이 옵니다. 팀원들과 프롬프트를 공유하고 싶거나, 회사 데이터가 AI 학습에 사용될까 걱정되거나, 관리자로서 직원들의 사용 현황을 파악하고 싶을 때가 그렇습니다. OpenAI는 이런 조직의 요구를 충족하기 위해 **Team** 과 **Enterprise** 요금제를 제공합니다.

* * *

## 요금제별 상세 비교

Team과 Enterprise는 이름은 비슷하지만 대상 조직 규모와 제공 기능에서 명확한 차이가 있습니다.

항목 | Team | Enterprise  
---|---|---  
가격 | 사용자당 월 $25 (연간 결제) / $30 (월간) | 별도 협의 (대규모 계약)  
최소 인원 | 2명 이상 | 통상 150명 이상 (기업 규모)  
GPT-4o 접근 | 무제한 | 무제한  
컨텍스트 창 | 32K | 128K  
데이터 학습 제외 | 기본 제외 | 기본 제외  
관리자 콘솔 | 기본 제공 | 고급 관리 기능  
SSO/SAML | 미지원 | 지원  
SCIM 프로비저닝 | 미지원 | 지원  
분석 대시보드 | 기본 통계 | 고급 분석  
GPTs 공유 범위 | 워크스페이스 내 | 워크스페이스 내 + 세분화 제어  
전담 지원 | 미지원 | 전담 계정 매니저  
Admin API | 미지원 | 지원  
  
tip

소규모 스타트업이나 중소기업이라면 Team 요금제로 시작하는 것이 현실적입니다. Enterprise는 SSO·SCIM 같은 IT 인프라 연동이 필요한 100명 이상 규모의 조직에 적합합니다.

* * *

## ChatGPT Team 도입 가이드

### Workspace 생성과 멤버 초대

Team 요금제 도입은 생각보다 간단합니다. 아래 절차를 따라 진행하세요.

**1단계: 워크스페이스 생성**

  1. [chat.openai.com](https://chat.openai.com) 접속 후 로그인
  2. 좌측 하단 계정 메뉴 → **Upgrade plan** 선택
  3. **ChatGPT Team** 선택 → 워크스페이스 이름 입력
  4. 결제 정보 입력 및 플랜 확정


**2단계: 멤버 초대**

워크스페이스가 생성되면 관리자 콘솔에서 멤버를 초대합니다.
    
    
    관리자 콘솔 접근 경로:
    Settings → Your plan → Manage workspace → Members
    

초대 방법은 두 가지입니다.

  * **이메일 초대** : 개별 이메일 주소 입력 후 초대 링크 발송
  * **초대 링크 공유** : 워크스페이스 전용 초대 링크를 생성해 팀 채널에 공유


tip

초대 링크는 만료 기한을 설정하거나 언제든 무효화할 수 있습니다. 보안을 위해 링크 공유 후 사용 완료 시 즉시 비활성화하는 습관을 들이세요.

### 관리자 콘솔 설정

관리자 콘솔(Admin Console)에서는 워크스페이스 전반을 제어할 수 있습니다.

**주요 설정 항목:**

  * **멤버 권한 관리** : 일반 멤버 / 관리자 역할 부여
  * **GPTs 공유 정책** : 멤버가 생성한 GPTs의 공유 범위 설정 (워크스페이스 전체 공개 또는 생성자만)
  * **데이터 정책 확인** : 학습 데이터 제외 여부 확인 (Team은 기본 제외)
  * **결제 및 사용량 확인** : 월별 사용 현황, 청구 내역 조회


### 팀 전용 Custom GPTs 생성과 공유

Team 요금제의 핵심 가치 중 하나는 **팀 전용 Custom GPTs를 만들어 워크스페이스 전체에 공유**할 수 있다는 점입니다.

**Custom GPT 생성 절차:**

  1. ChatGPT 상단 메뉴 → **Explore GPTs** → **Create** 클릭
  2. GPT Builder에서 이름, 설명, 지침(Instructions) 작성
  3. Knowledge 파일 업로드 (사내 문서, 매뉴얼 등)
  4. 저장 시 공개 범위를 **"Only people in [워크스페이스명]"** 으로 설정


이렇게 만든 GPTs는 워크스페이스 멤버 전원이 Explore GPTs 화면에서 바로 사용할 수 있습니다.

* * *

## Enterprise 전용 기능

Enterprise 요금제는 대규모 조직의 IT 운영 요구사항을 충족하는 고급 기능을 제공합니다.

### SSO(Single Sign-On) 설정

SSO는 직원들이 회사 계정(Google Workspace, Microsoft Azure AD 등) 하나로 ChatGPT에 로그인할 수 있도록 합니다.
    
    
    지원 SSO 방식:
    - SAML 2.0
    - OIDC (OpenID Connect)
    
    연동 가능 IdP:
    - Okta
    - Microsoft Azure Active Directory
    - Google Workspace
    - OneLogin
    

설정 방법은 OpenAI Enterprise 담당자와 협력하여 SAML 메타데이터를 교환하는 방식으로 진행됩니다.

### SCIM 프로비저닝

SCIM(System for Cross-domain Identity Management)을 통해 조직의 사용자 관리 시스템과 ChatGPT를 연동할 수 있습니다.

  * 신규 직원 입사 시 자동으로 ChatGPT 계정 생성
  * 퇴사 직원 계정 자동 비활성화
  * 부서 변경 시 권한 자동 업데이트


이를 통해 IT 관리자의 수동 작업을 크게 줄일 수 있습니다.

### 데이터 보존 정책

Enterprise에서는 대화 데이터의 보존 기간을 조직 정책에 맞게 설정할 수 있습니다.

  * 특정 기간 후 자동 삭제 설정
  * 컴플라이언스 요구사항(GDPR, HIPAA 등)에 맞는 정책 적용
  * 감사 로그(Audit Log) 보관 및 조회


### 분석 대시보드

관리자는 고급 분석 대시보드를 통해 조직 전체의 AI 활용 현황을 파악할 수 있습니다.

  * 부서별 / 사용자별 사용량 통계
  * 자주 사용되는 GPTs 순위
  * 시간대별 접속 패턴
  * 비용 분석 리포트


### Admin API

Admin API를 통해 워크스페이스 관리를 자동화할 수 있습니다.
    
    
    # Admin API 활용 예시: 멤버 목록 조회
    import requests
    
    headers = {
        "Authorization": f"Bearer {ADMIN_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(
        "https://api.openai.com/v1/organization/users",
        headers=headers
    )
    
    users = response.json()
    print(f"총 멤버 수: {len(users['data'])}")
    

* * *

## Custom GPTs로 사내 지식 베이스 구축

ChatGPT Team/Enterprise의 Custom GPTs 기능을 활용하면 조직의 지식을 AI화하여 전 직원이 쉽게 활용할 수 있습니다.

### 부서별/업무별 GPTs 설계

모든 것을 하나의 GPT로 만들려 하지 말고, 업무 단위로 특화된 GPTs를 설계하세요.

부서 | GPT 이름 | 주요 역할  
---|---|---  
인사팀 | HR 어시스턴트 | 취업규칙 안내, 휴가 정책 Q&A  
영업팀 | 제안서 도우미 | 제품 설명서 기반 제안서 초안 작성  
개발팀 | 코드 리뷰어 | 사내 코딩 컨벤션 기반 코드 검토  
고객지원 | CS 봇 | FAQ, 에스컬레이션 가이드라인  
  
### Knowledge 파일 관리 전략

Custom GPT의 Knowledge 섹션에 업로드하는 파일이 AI의 답변 품질을 결정합니다.

**효과적인 Knowledge 파일 구성:**

  * **파일 형식** : PDF, DOCX, TXT, Markdown 모두 지원 (최대 20개, 파일당 512MB)
  * **문서 최신화** : 정책 변경 시 즉시 Knowledge 파일 업데이트
  * **구조화된 작성** : 목차와 헤딩이 명확한 문서일수록 AI가 더 정확하게 참조


    
    
    Knowledge 파일 명명 규칙 예시:
    - [HR]_취업규칙_v2024.pdf
    - [영업]_제품카탈로그_2024Q4.pdf
    - [공통]_사내보안정책_v3.docx
    

### 사용 가이드라인 수립

GPT 배포 시 반드시 사용 가이드라인을 함께 제공하세요.

  * GPT의 용도와 한계 명시 ("이 GPT는 초안 작성 보조 도구입니다. 최종 검토는 반드시 담당자가 수행하세요.")
  * 입력하면 안 되는 정보 안내 (고객 개인정보, 비밀 계약 내용 등)
  * 오류 발견 시 피드백 채널 안내


* * *

## 도입 로드맵

조직 전체에 AI를 성공적으로 정착시키려면 단계적 접근이 중요합니다.

### Phase 1: 파일럿 (1~2개월)

**소규모 팀 5~15명을 선정해 시범 도입**합니다. 이 단계의 목표는 효과 검증과 문제점 파악입니다.

  * AI 활용에 관심 있는 얼리어답터 위주로 구성
  * 명확한 사용 사례(Use Case) 2~3개 선정 후 집중
  * 주간 피드백 미팅으로 개선사항 수집
  * KPI 기준 수립 (시간 절약, 산출물 품질 등)


### Phase 2: 확대 (2~4개월)

파일럿의 성과를 기반으로 **부서 단위로 도입 범위를 확대**합니다.

  * 파일럿 참여자를 각 부서의 챔피언으로 활용
  * 부서별 특화 Custom GPTs 개발
  * 보안 정책 및 사용 지침 공식화
  * 교육 프로그램 운영


### Phase 3: 전사 확산 (4개월 이후)

전 직원을 대상으로 확산하되, **강제가 아닌 자발적 참여 문화 조성**에 집중합니다.

  * AI 활용 성과 사례 내부 공유 (뉴스레터, 타운홀)
  * 우수 활용 사례 시상 및 인정
  * 지속적인 교육과 새로운 기능 업데이트 공유


* * *

## 사내 교육 전략과 챔피언 프로그램

기술 도입만으로는 충분하지 않습니다. 사람이 변해야 조직이 변합니다.

**챔피언 프로그램 운영 방법:**

챔피언(Champion)은 각 부서에서 AI 활용을 앞장서서 전파하는 내부 전도사입니다.

  1. **선발** : 부서별 1~2명, AI에 관심 있고 동료들과 소통을 좋아하는 직원
  2. **집중 교육** : 일반 직원보다 심화된 교육 제공 (프롬프트 엔지니어링, GPT 구축 등)
  3. **정기 모임** : 월 1회 챔피언 커뮤니티 미팅으로 사례 공유
  4. **권한 부여** : 부서 전용 GPT 관리 권한, 새 기능 선행 테스트 기회 제공


**교육 커리큘럼 예시:**

대상 | 교육 내용 | 시간  
---|---|---  
전 직원 기초 | ChatGPT 기본 사용법, 보안 주의사항 | 2시간  
직무별 심화 | 업무 특화 프롬프트, 사내 GPT 활용 | 4시간  
챔피언 과정 | GPT 구축, 프롬프트 최적화, 성과 측정 | 8시간  
  
tip

교육은 일회성 이벤트가 아닌 지속적인 과정으로 설계하세요. ChatGPT는 빠르게 발전하고 있어 분기별 업데이트 교육이 효과적입니다.

---

**원본**: https://wikidocs.net/340839  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:09 오후**
