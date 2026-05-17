#!/usr/bin/env node
import React from 'react';
import {render} from 'ink';
import meow from 'meow';
import App from './app.js';

const cli = meow(
	`
		Usage
		  $ React-ink-demo2

		Options
			--name  Your name

		Examples
		  $ React-ink-demo2 --name=Jane
		  Hello, Jane
	`,
	{
		importMeta: import.meta,
	},
);

const {waitUntilExit} = render(<App name={cli.flags.name} />);

await waitUntilExit();

console.log('App exited');
