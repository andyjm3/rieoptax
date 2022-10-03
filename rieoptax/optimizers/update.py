import jax 

from core import ManifoldArray

def apply_update(params, updates):
    """Applies an update to the corresponding parameters."""
    return jax.tree_map(lambda p,u : ManifoldArray(p.manifold.exp(u), p.manifold), params, updates)
