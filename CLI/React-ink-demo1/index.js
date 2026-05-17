import React, { useEffect, useState } from 'react';
import { render, Text } from 'ink';

const Counter = () =>{
    const [counter, setCounter] = useState(0);

    useEffect(() => {
        const timer = setInterval(()=>{
            setCounter(previousCounter=>previousCounter +1);
        }, 100);

        return ()=>{
            clearInterval(timer);
        }
    }, []);

    return <Text color="green">{counter} test passed</Text>
}

render(<Counter/>);

/*
*React 的核心模型：state变化->触发re-render->重新执行组件函数->生成新的jsx->React diff（比较“新旧 UI”，只更新变了的部分）->更新UI
*
*useState:状态变量(counter)一旦发生变化，组件的视图UI也会发生变化
*
* useEffect（副作用） = “在组件渲染之后做额外事情的地方”
*
* render（组件函数） = 负责画 UI
*
*setInterval = 每隔一段时间重复执行某段代码
*
*clearInterval(定时器ID) = 停止定时器
*
* 步骤：先画 UI（0）->useEffect执行（启动定时器）->定时器执行（每100ms更新counter）->state变化（触发重新渲染）->重复上面步骤->...->Ctrl+C(退出卸载组件)->执行clearInterval停止计时
* */