import React from 'react';

const MatrixStatus = ({ loading, metrics }) => (
  <div>Matrix ready: {metrics.ready}</div>
);
export default MatrixStatus;
