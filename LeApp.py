import sys
import getopt
from Logger.Logger import Logger
from Palette.ToolBar import ToolBar
from selenium import webdriver
from ProjectParser.Parser import Parser


def main():

    if len(sys.argv) == 1:
        Logger.error(f"Run with '-h' option to see the possible options!")
        sys.exit(0)

    arguments = sys.argv.copy()
    for index, arg in enumerate(sys.argv):
        if arg == '-h' or arg == '-e' or arg == '-i':
            arguments.insert(index+1, ' ')

    try:
        opts, args = getopt.getopt(arguments[1:], "h:f:i:e:")
    except getopt.GetoptError as ex:
        Logger.error(f"You provided unsupportde option:\n\t{ex.msg}")
        return

    for option, argument in opts:
        if ('-h') in option:
            Logger.info("You are usnig LeApp.\n\n\t -f <filename>.json - to load project from the file. \n\t -i - interactive mode. \n\t -e - to run examples.\n")
        if ('-f') in option:
            driver = webdriver.Firefox()
            driver.get("https://ainak.gitlab.io/leapp-app/")
            ToolBar.save_project(driver)
            parser = Parser(argument)
            parser.load_project()
            ToolBar.load_project(driver, parser)
            sys.exit(0)
        if ("-i") in option:
            Logger.warning("Interactive mode is not implemented. Need more ideas for that.")
            sys.exit(0)
        if ("-e") in option:
            from SupportScripts.Examples import Example
            driver = webdriver.Firefox()
            driver.get("https://ainak.gitlab.io/leapp-app/") 
            Example.run(driver)
            sys.exit(0)


if __name__ == "__main__":
    main()
    
