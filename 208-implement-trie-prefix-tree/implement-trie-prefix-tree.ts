class Trie {
    private data;

    constructor() {
        this.data = {};
    }

    insert(word: string): void {
        let curr = this.data;
        for (let i = 0; i < word.length; i++) {
            if (curr[word[i]]) {
                curr = curr[word[i]];
            } else {
                curr = curr[word[i]] = {};
            }
        }
        curr["end"] = true;
    }

    search(word: string): boolean {
        let curr = this.data;
        let found = true;
        for (let i = 0; i < word.length; i++) {
            if (curr[word[i]]) {
                curr = curr[word[i]];
            } else {
                found = false;
                break;
            }
        }
        if (found) {
            return !!curr["end"];
        }
        return false;
    }

    startsWith(prefix: string): boolean {
        let curr = this.data;
        let found = true;
        for (let i = 0; i < prefix.length; i++) {
            if (curr[prefix[i]]) {
                curr = curr[prefix[i]];
            } else {
                found = false;
                break;
            }
        }
        return found;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */