const { execSync } = require('child_process');

const tool = 'eslint'; 
const filePath = '1.js';

let command = '';

if (tool === 'prettier') {
    command = `prettier --write ${filePath}`;
} else if (tool === 'eslint') {
    command = `eslint --fix ${filePath}`;
} else if (tool === 'standard') {
    command = `standard --fix ${filePath}`;
} else if (tool === 'js-beautify') {
    command = `js-beautify -r ${filePath}`;
} else {
    console.error('Unsupported formatting tool specified.');
    process.exit(1);
}

const startTime = Date.now();

try {
    execSync(command, { stdio: 'inherit' });
    const endTime = Date.now();
    console.log(`Formátovanie trvalo ${(endTime - startTime) / 1000} sekúnd.`);
} catch (error) {
    console.error('Formátovanie zlyhalo:', error.message);
    process.exit(1);
}
