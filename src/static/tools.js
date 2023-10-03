function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function replace(url, delay = 0) {
    await sleep(delay)
    window.location.replace(url)
}