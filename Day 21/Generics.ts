'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;
process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

function main() {
    // Enter your code here
    function printArray<T>(array: T[]): void {
        array.forEach(element => console.log(element));
    }

    const n = parseInt(readLine().trim());
    const intArray: number[] = [];
    for (let i = 0; i < n; i++) {
        intArray.push(parseInt(readLine().trim()));
    }
    
    const m = parseInt(readLine().trim());
    const stringArray: string[] = [];
    for (let i = 0; i < m; i++) {
        stringArray.push(readLine().trim());
    }

    printArray(intArray);
    printArray(stringArray);
    
}
