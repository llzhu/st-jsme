import React, { useEffect } from "react";
import { Jsme } from 'jsme-react'

import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib";

interface JsmeArgs {
  width: string;
  height: string;
  init_smiles: string;
}


export class StJsme extends  StreamlitComponentBase {
  logSmiles(smiles) {
    console.log(smiles)
    Streamlit.setComponentValue(smiles)
  }

  render () {
    const {width, height, init_smiles} :JsmeArgs = this.props.args

    return (
        <Jsme height={height} width={width} smiles={init_smiles} options="oldlook,star" onChange={this.logSmiles} />
    )
  }
}

// Link the component to Streamlit JS events.
export default withStreamlitConnection(StJsme);