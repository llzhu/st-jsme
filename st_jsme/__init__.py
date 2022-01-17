import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component("st_jsme", url="http://localhost:3001" )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_jsme", path=build_dir)


def st_jsme(width: str, height: str, init_smile: str, key=None) -> str:
    component_value = _component_func(width=width, height=height, init_smiles=init_smile, key=key)
    return component_value

