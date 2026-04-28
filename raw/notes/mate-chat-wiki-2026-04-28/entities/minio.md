---
title: "MinIO"
type: entity
source_count: 2
tags: [storage, minio, s3, file-upload, object-storage]
related:
  - "../entities/fastapi-app.md"
  - "../entities/docker-infrastructure.md"
---

# MinIO

## Overview

Mate Chat의 파일 저장소로, S3 호환 API를 제공하는 자체 호스팅 객체 스토리지이다. Firebase Storage를 대체하며, 프로필 이미지, 채팅방 이미지, 채팅 첨부파일을 저장한다.

## Architecture/Structure

### 버킷 구조

```
mate-chat/
├── profiles/{user_id}/{filename}
├── chatrooms/{room_id}/{filename}
└── messages/{room_id}/{message_id}/{filename}
```

## Key Details

- **S3 호환**: boto3 클라이언트로 접근, AWS S3로 이전 용이
- **자체 호스팅**: Docker 컨테이너로 운영
- **개발 환경**: `localhost:9001` (MinIO Console)
- **환경 변수**: `MINIO_ENDPOINT`, `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`, `MINIO_BUCKET_NAME`

## Dependencies

- boto3 (Python S3 클라이언트)
- Docker (컨테이너 실행)

## Known Issues

- 이미지 리사이징 연동 미구현 (가능성만 언급)
- 프로덕션에서 MinIO Cluster 구성 또는 AWS S3 전환 필요

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- 파일 업로드 API
- [Docker Infrastructure](../entities/docker-infrastructure.md) -- 컨테이너 배포
