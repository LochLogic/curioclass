/**
 * Safe WGSL minifier for staying well under the 2 MB single-file budget.
 * Strips comments and redundant whitespace while keeping all WGSL tokens valid.
 */
export function minifyWgsl(source) {
  // Remove block comments and single-line comments
  let out = source
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/\/\/[^\n]*/g, '');

  // Collapse whitespace runs to a single space
  out = out.replace(/\s+/g, ' ').trim();

  // Remove spaces around punctuation where safe in WGSL
  out = out
    .replace(/\s*([{}()\[\],;:])\s*/g, '$1')
    .replace(/\s*(=|==|!=|<=|>=|\+=|-=|\*=|\/=|->|&&|\|\|)\s*/g, '$1')
    .replace(/\s*([+\-*\/%<>&|^!~])\s*/g, '$1');

  // Restore required space after keywords that may precede '(' or identifiers
  out = out.replace(/\b(return|var|let|const|fn|struct|alias|override|if|else|for|while|loop|switch|case|default)\b(?=[A-Za-z0-9_@])/g, '$1 ');

  // Compact trivial trailing zero decimals like 1.0 -> 1. (when not followed by digits/ident)
  out = out.replace(/(\b\d+)\.0\b(?![fhu0-9A-Za-z_])/g, '$1.');

  return out;
}
