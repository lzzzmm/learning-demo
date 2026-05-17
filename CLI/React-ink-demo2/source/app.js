import React, {useState} from 'react';
import {Text, useInput, useApp, Box} from 'ink';

export default function App({name = 'Stranger'}) {
	const {exit} = useApp();
	const [input, setInput] = useState('');
	const [messages, setMessages] = useState([
		{
			role: 'bot',
			content: `Hello, ${name}`
		}
	]);


	useInput((value, key) => {
		if (key.escape || value === 'q') {
			exit();
			return;
		}

		// 回车发送
		if(key.return){
			const userMessage = {
				role: name,
				content: input
			};

			// 模拟 AI 回复
			const botMessage = {
				role: 'bot',
				content: `你刚刚说的是: ${input}`
			};

			setMessages(prev => [
				...prev,
				userMessage,
				botMessage
			]);

			setInput('');
			return;
		}
	});


	return(
		<Box flexDirection="column">
			{/* 聊天记录 */}
			{messages.map((msg, index) => (
				<Text key={index}>
					{msg.role === 'user' ? 'You' : 'Bot'}:
					{' '}
					<Text color={msg.role === 'user' ? 'cyan' : 'green'}>
						{msg.content}
					</Text>
				</Text>
			))}

			{/* 输入框 */}
			<Text>
				<Text color="yellow">You: </Text>
				{input}
			</Text>
		</Box>
	);
}
