import React, { useEffect, useState } from 'react';
import { render, Text } from 'ink';
const Counter = () => {
  const [counter, setCounter] = useState(0);
  useEffect(() => {
    const timer = setInterval(() => {
      console.log('定时器执行中...');
      setCounter(previousCounter => previousCounter + 1);
    }, 100);
    return () => {
      clearInterval(timer);
    };
  }, []);
  return /*#__PURE__*/React.createElement(Text, {
    color: "green"
  }, counter, " test passed");
};
render(/*#__PURE__*/React.createElement(Counter, null));
