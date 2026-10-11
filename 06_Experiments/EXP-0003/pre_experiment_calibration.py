import json, os, sys, time, resource
import torch
sys.path.insert(0, '/workspace/lithography---research-fd-nig')
from tools.fd_nig_reference import make_fixture, exhaustive_aggregate, pair_products as ref_products
from tools.fd_nig_aggregation import aggregate, route_pairs, absolute_scales

SEED=20261011
out=[]
for n in (4,8):
  base=make_fixture(seed=SEED,height=n,width=n)
  for dtype in (torch.complex64, torch.complex128):
    spectrum=base.spectrum.to(dtype)
    coeff=base.coefficients.to(dtype)
    pairs=base.pairs
    # independent high precision reference, then same precision reference
    t0=time.perf_counter(); ref_hi=exhaustive_aggregate(base.coefficients,base.spectrum,pairs); tref_hi=time.perf_counter()-t0
    t0=time.perf_counter(); ref=exhaustive_aggregate(coeff,spectrum,pairs); tref=time.perf_counter()-t0
    t0=time.perf_counter(); cand=aggregate(coeff,spectrum,pairs); tcand=time.perf_counter()-t0
    cand2=aggregate(coeff,spectrum,pairs)
    bins=route_pairs(pairs,n,n)
    contrib=ref_products(coeff,spectrum,pairs)
    scales=absolute_scales(contrib,bins,n*n).reshape(n,n)
    abs_err=(cand-ref).abs(); hi_err=(cand-ref_hi.to(dtype)).abs()
    bound=1e-6+1e-5*scales if dtype==torch.complex64 else 1e-12+1e-12*scales
    zero_safe=abs_err-bound
    flat=abs_err.flatten(); sf=scales.flatten()
    nz=sf>0
    cancel_idx=torch.argmin(torch.where(nz,sf,torch.full_like(sf,float('inf'))))
    empty_count=int((sf==0).sum())
    out.append(dict(grid=n,dtype=str(dtype),max_abs=float(abs_err.max()),max_hi_abs=float(hi_err.max()),max_zero_safe_excess=float(zero_safe.max()),max_scale=float(scales.max()),cancellation_bin=int(cancel_idx),cancellation_error=float(abs_err.flatten()[cancel_idx]),cancellation_scale=float(sf.flatten()[cancel_idx]),empty_bins=empty_count,reference_seconds=tref,candidate_seconds=tcand,high_precision_reference_seconds=tref_hi,repeatable=bool(torch.equal(cand,cand2))))
print(json.dumps({'seed':SEED,'results':out,'peak_rss_kb':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
