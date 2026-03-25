from dataclasses import replace

from guppylang_internals.tys.const import ExistentialConstVar
from guppylang_internals.tys.subst import Subst, Substituter


def zonk_const_ty(ex: ExistentialConstVar, subst: Subst) -> ExistentialConstVar:
    """Apply a substitution to the type variables of the ExistentialConstVar,
    without substituting the var itself."""
    return replace(ex, ty=ex.ty.transform(Substituter(subst)))
