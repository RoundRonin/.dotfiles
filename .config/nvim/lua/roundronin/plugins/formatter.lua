return {
    -- {
    --     'mhartington/formatter.nvim',
    --     config = function()
    --         -- Utilities for creating configurations
    --         local util = require "formatter.util"
    --
    --         local nmap = function(keys, func, desc)
    --             if desc then
    --                 desc = 'Formatter: ' .. desc
    --             end
    --
    --             vim.keymap.set('n', keys, func, { desc = desc })
    --         end
    --
    --         -- Provides the Format, FormatWrite, FormatLock, and FormatWriteLock commands
    --         require("formatter").setup {
    --             -- Enable or disable logging
    --             logging = true,
    --             -- Set the log level
    --             log_level = vim.log.levels.WARN,
    --             -- All formatter configurations are opt-in
    --             filetype = {
    --                 -- Use the special "*" filetype for defining formatter configurations on
    --                 -- any filetype
    --                 ["*"] = {
    --                     -- "formatter.filetypes.any" defines default configurations for any
    --                     -- filetype
    --                     require("formatter.filetypes.any").lsp_format,
    --                     require("formatter.filetypes.any").remove_trailing_whitespace,
    --                 }
    --             }
    --         }
    --     end,
    -- }
}