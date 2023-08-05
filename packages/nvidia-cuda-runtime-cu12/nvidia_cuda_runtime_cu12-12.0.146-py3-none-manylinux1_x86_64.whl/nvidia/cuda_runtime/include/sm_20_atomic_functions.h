/*
 * Copyright 1993-2014 NVIDIA Corporation.  All rights reserved.
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

#if !defined(__SM_20_ATOMIC_FUNCTIONS_H__)
#define __SM_20_ATOMIC_FUNCTIONS_H__

#if defined(__CUDACC_RTC__)
#define __SM_20_ATOMIC_FUNCTIONS_DECL__ __device__
#elif defined(_NVHPC_CUDA)
#define __SM_20_ATOMIC_FUNCTIONS_DECL__ extern __device__ __cudart_builtin__
#else /* __CUDACC_RTC__ */
#define __SM_20_ATOMIC_FUNCTIONS_DECL__ static __inline__ __device__
#endif /* __CUDACC_RTC__ */

#if defined(__cplusplus) && defined(__CUDACC__)

/*******************************************************************************
*                                                                              *
*                                                                              *
*                                                                              *
*******************************************************************************/

#include "cuda_runtime_api.h"

#if defined(_NVHPC_CUDA)
#undef __device_builtin__
#define __device_builtin__ __location__(device) __location__(host)
#endif /* _NVHPC_CUDA */

/* Add !defined(_NVHPC_CUDA) to avoid empty function definition in CUDA
 * C++ compiler where the macro __CUDA_ARCH__ is not defined. */
#if !defined(__CUDA_ARCH__) && !defined(_NVHPC_CUDA)
#define __DEF_IF_HOST { }
#else  /* !__CUDA_ARCH__ */
#define __DEF_IF_HOST ;
#endif /* __CUDA_ARCH__ */


#if defined(__CUDA_ARCH__) || defined(_NVHPC_CUDA)
extern "C"
{
extern __device__ __device_builtin__ float __fAtomicAdd(float *address, float val);
}
#endif /* __CUDA_ARCH__ */

#if defined(_NVHPC_CUDA)
#undef __device_builtin__
#define __device_builtin__
#endif /* _NVHPC_CUDA */

/*******************************************************************************
*                                                                              *
*                                                                              *
*                                                                              *
*******************************************************************************/

__SM_20_ATOMIC_FUNCTIONS_DECL__ float atomicAdd(float *address, float val) __DEF_IF_HOST

#endif /* __cplusplus && __CUDACC__ */

#undef __DEF_IF_HOST
#undef __SM_20_ATOMIC_FUNCTIONS_DECL__

#if !defined(__CUDACC_RTC__) && (defined(__CUDA_ARCH__) || defined(_NVHPC_CUDA))
#include "sm_20_atomic_functions.hpp"
#endif /* !__CUDACC_RTC__ && defined(__CUDA_ARCH__) || defined(_NVHPC_CUDA) */

#endif /* !__SM_20_ATOMIC_FUNCTIONS_H__ */
