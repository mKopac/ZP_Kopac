const { execSync } = require('child_process');

command = `prettier --write 1.js`;
// prettier --write 1.js
// eslint --fix 1.js
// standard --fix 1.js
// js-beautify -r 1.js

const startTime = Date.now();

try {
    execSync(command, { stdio: 'inherit' });
    const endTime = Date.now();
    console.log(`Formátovanie trvalo ${(endTime - startTime) / 1000} sekúnd.`);
} catch (error) {
    console.error('Formátovanie zlyhalo:', error.message);
    process.exit(1);
}
