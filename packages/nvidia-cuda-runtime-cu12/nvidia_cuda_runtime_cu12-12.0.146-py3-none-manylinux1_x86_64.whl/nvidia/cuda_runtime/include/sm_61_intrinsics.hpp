/*
 * Copyright 2016 NVIDIA Corporation.  All rights reserved.
 *
 * NOTICE TO LICENSEE:
 *
 * This source code and/or documentation ("Licensed Deliverables") are
 * subject to NVIDIA intellectual property rights under U.S. and
 * international Copyright laws.
 *
 * These Licensed Deliverables contained herein is PROPRIETARY and
 * CONFIDENTIAL to NVIDIA and is being provided under the terms and
 * conditions of a form of NVIDIA software license agreement by and
 * between NVIDIA and Licensee ("License Agreement") or electronically
 * accepted by Licensee.  Notwithstanding any terms or conditions to
 * the contrary in the License Agreement, reproduction or disclosure
 * of the Licensed Deliverables to any third party without the express
 * written consent of NVIDIA is prohibited.
 *
 * NOTWITHSTANDING ANY TERMS OR CONDITIONS TO THE CONTRARY IN THE
 * LICENSE AGREEMENT, NVIDIA MAKES NO REPRESENTATION ABOUT THE
 * SUITABILITY OF THESE LICENSED DELIVERABLES FOR ANY PURPOSE.  IT IS
 * PROVIDED "AS IS" WITHOUT EXPRESS OR IMPLIED WARRANTY OF ANY KIND.
 * NVIDIA DISCLAIMS ALL WARRANTIES WITH REGARD TO THESE LICENSED
 * DELIVERABLES, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY,
 * NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
 * NOTWITHSTANDING ANY TERMS OR CONDITIONS TO THE CONTRARY IN THE
 * LICENSE AGREEMENT, IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY
 * SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, OR ANY
 * DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
 * WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
 * ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
 * OF THESE LICENSED DELIVERABLES.
 *
 * U.S. Government End Users.  These Licensed Deliverables are a
 * "commercial item" as that term is defined at 48 C.F.R. 2.101 (OCT
 * 1995), consisting of "commercial computer software" and "commercial
 * computer software documentation" as such terms are used in 48
 * C.F.R. 12.212 (SEPT 1995) and is provided to the U.S. Government
 * only as a commercial end item.  Consistent with 48 C.F.R.12.212 and
 * 48 C.F.R. 227.7202-1 through 227.7202-4 (JUNE 1995), all
 * U.S. Government End Users acquire the Licensed Deliverables with
 * only those rights set forth herein.
 *
 * Any use of the Licensed Deliverables in individual and commercial
 * software must include, in the user documentation and internal
 * comments to the code, the above Disclaimer and U.S. Government End
 * Users Notice.
 */

#if !defined(__SM_61_INTRINSICS_HPP__)
#define __SM_61_INTRINSICS_HPP__

#if defined(__CUDACC_RTC__)
#define __SM_61_INTRINSICS_DECL__ __device__
#else /* !__CUDACC_RTC__ */
#define __SM_61_INTRINSICS_DECL__ static __device__ __inline__
#endif /* __CUDACC_RTC__ */

#if defined(__cplusplus) && defined(__CUDACC__)

#if defined(_NVHPC_CUDA) || !defined(__CUDA_ARCH__) || __CUDA_ARCH__ >= 610

/*******************************************************************************
*                                                                              *
*                                                                              *
*                                                                              *
*******************************************************************************/

#include "cuda_runtime_api.h"

/*******************************************************************************
*                                                                              *
*  Below are implementations of SM-6.1 intrinsics which are included as        *
*  source (instead of being built in to the compiler)                          *
*                                                                              *
*******************************************************************************/

// 4a
__SM_61_INTRINSICS_DECL__ int __dp4a(int srcA, int srcB, int c) {
    int ret;
    asm volatile ("dp4a.s32.s32 %0, %1, %2, %3;" : "=r"(ret) : "r"(srcA), "r"(srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ unsigned int __dp4a(unsigned int srcA, unsigned int srcB, unsigned int c) {
    unsigned int ret;
    asm volatile ("dp4a.u32.u32 %0, %1, %2, %3;" : "=r"(ret) : "r"(srcA), "r"(srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ int __dp4a(char4 srcA, char4 srcB, int c) {
    int ret;
    asm volatile ("dp4a.s32.s32 %0, %1, %2, %3;" : "=r"(ret) : "r"(*(int *)&srcA), "r"(*(int *)&srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ unsigned int __dp4a(uchar4 srcA, uchar4 srcB, unsigned int c) {
    unsigned int ret;
    asm volatile ("dp4a.u32.u32 %0, %1, %2, %3;" : "=r"(ret) : "r"(*(unsigned int *)&srcA), "r"(*(unsigned int *)&srcB), "r"(c));
    return ret;
}

// 2a.lo
__SM_61_INTRINSICS_DECL__ int __dp2a_lo(int srcA, int srcB, int c) {
    int ret;
    asm volatile ("dp2a.lo.s32.s32 %0, %1, %2, %3;" : "=r"(ret) : "r"(srcA), "r"(srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ unsigned int __dp2a_lo(unsigned int srcA, unsigned int srcB, unsigned int c) {
    unsigned int ret;
    asm volatile ("dp2a.lo.u32.u32 %0, %1, %2, %3;" : "=r"(ret) : "r"(srcA), "r"(srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ int __dp2a_lo(short2 srcA, char4 srcB, int c) {
    int ret;
    asm volatile ("dp2a.lo.s32.s32 %0, %1, %2, %3;" : "=r"(ret) : "r"(*(int *)&srcA), "r"(*(int *)&srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ unsigned int __dp2a_lo(ushort2 srcA, uchar4 srcB, unsigned int c) {
    unsigned int ret;
    asm volatile ("dp2a.lo.u32.u32 %0, %1, %2, %3;" : "=r"(ret) : "r"(*(unsigned int *)&srcA), "r"(*(unsigned int *)&srcB), "r"(c));
    return ret;
}

// 2a.hi
__SM_61_INTRINSICS_DECL__ int __dp2a_hi(int srcA, int srcB, int c) {
    int ret;
    asm volatile ("dp2a.hi.s32.s32 %0, %1, %2, %3;" : "=r"(ret) : "r"(srcA), "r"(srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ unsigned int __dp2a_hi(unsigned int srcA, unsigned int srcB, unsigned int c) {
    unsigned int ret;
    asm volatile ("dp2a.hi.u32.u32 %0, %1, %2, %3;" : "=r"(ret) : "r"(srcA), "r"(srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ int __dp2a_hi(short2 srcA, char4 srcB, int c) {
    int ret;
    asm volatile ("dp2a.hi.s32.s32 %0, %1, %2, %3;" : "=r"(ret) : "r"(*(int *)&srcA), "r"(*(int *)&srcB), "r"(c));
    return ret;
}

__SM_61_INTRINSICS_DECL__ unsigned int __dp2a_hi(ushort2 srcA, uchar4 srcB, unsigned int c) {
    unsigned int ret;
    asm volatile ("dp2a.hi.u32.u32 %0, %1, %2, %3;" : "=r"(ret) : "r"(*(unsigned int *)&srcA), "r"(*(unsigned int *)&srcB), "r"(c));
    return ret;
}


#endif /* _NVHPC_CUDA || !__CUDA_ARCH__ || __CUDA_ARCH__ >= 610 */

#endif /* __cplusplus && __CUDACC__ */

#undef __SM_61_INTRINSICS_DECL__

#endif /* !__SM_61_INTRINSICS_HPP__ */

