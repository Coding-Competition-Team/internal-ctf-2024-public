const readline = require('node:readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function safe(str) {
  if (str.includes(';') || str.includes("'") || str.includes('"') || str.includes('`')) 
    return false;

  if (str.toLowerCase().includes('read') || str.toLowerCase().includes('open'))
    return false;

  return true;
}

async function main() {
  console.log(`Welcome to NodeJail! Try to get the flag (impossible).`)
  await new Promise(resolve => setTimeout(resolve, 800));
  console.log(`Running example code...`)
  console.log(`> console.log("Hello World!")`)
  await new Promise(resolve => setTimeout(resolve, 200));
  console.log("Hello World!");

  rl.question(`> `, code => {
    if (!safe(code)) {
      console.log('Invalid characters detected.');
      rl.close();
      return;
    }
    eval(code);
    rl.close();
  });

  return
}

main();