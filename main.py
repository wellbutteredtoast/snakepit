import pygame
import sys
import time

import score

from games.game1 import game1
from games.game2 import game2
from games.game3 import game3
from games.asteroids.game import muncss_entry

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (50, 50, 50)
MENU_TITLE_COLOR = (255, 215, 0)
MENU_ITEM_COLOR = (200, 200, 200)
MENU_ITEM_HOVER_COLOR = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snakepit")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont(None, 72)
    menu_font = pygame.font.SysFont(None, 48)

    current_score = score.init_score()

    games = [
        {"name": "Red Clicker", "module": game1},
        {"name": "Blue Clicker", "module": game2},
        {"name": "Green Clicker", "module": game3},
        {"name": "Asteroids", "module": muncss_entry},
    ]

    menu_state = {
        "active": True,
        "selected_index": 0,
    }

    active_game = {"module": None, "state": None}

    last_time = time.time()
    running = True

    while running:
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if menu_state["active"]:
                handle_menu_events(event, menu_state, games, active_game, screen)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Return to menu
                if active_game["module"]:
                    active_game["module"].game_shutdown(active_game["state"])
                    active_game["module"] = None
                    active_game["state"] = None
                    menu_state["active"] = True

        if menu_state["active"]:
            render_menu(screen, title_font, menu_font, menu_state, games, current_score)
        else:
            if active_game["module"] and active_game["state"]:
                active_game["state"], score_change = active_game["module"].game_update(
                    screen, active_game["state"], events, dt, current_score
                )
                if score_change != 0:
                    current_score = score.update_score(current_score, score_change)

        pygame.display.flip()
        clock.tick(FPS)

    if active_game["module"] and active_game["state"]:
        active_game["module"].game_shutdown(active_game["state"])

    pygame.quit()
    sys.exit()


def handle_menu_events(event, menu_state, games, active_game, screen):
    """Handle events in the menu state."""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            menu_state["selected_index"] = (menu_state["selected_index"] - 1) % len(
                games
            )
        elif event.key == pygame.K_DOWN:
            menu_state["selected_index"] = (menu_state["selected_index"] + 1) % len(
                games
            )
        elif event.key == pygame.K_RETURN:
            selected_game = games[menu_state["selected_index"]]
            active_game["module"] = selected_game["module"]
            active_game["state"] = active_game["module"].game_init(screen)
            menu_state["active"] = False


def render_menu(screen, title_font, menu_font, menu_state, games, current_score):
    """Render the main menu."""
    screen.fill(BACKGROUND_COLOR)

    title_text = title_font.render("Snakepit", True, MENU_TITLE_COLOR)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title_text, title_rect)

    score_text = menu_font.render(
        score.format_score(current_score), True, MENU_TITLE_COLOR
    )
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 170))
    screen.blit(score_text, score_rect)

    for i, game in enumerate(games):
        color = (
            MENU_ITEM_HOVER_COLOR
            if i == menu_state["selected_index"]
            else MENU_ITEM_COLOR
        )
        game_text = menu_font.render(game["name"], True, color)
        text_rect = game_text.get_rect(center=(SCREEN_WIDTH // 2, 250 + i * 70))
        screen.blit(game_text, text_rect)

        if i == menu_state["selected_index"]:
            pygame.draw.polygon(
                screen,
                color,
                [
                    (text_rect.left - 20, text_rect.centery),
                    (text_rect.left - 40, text_rect.centery - 10),
                    (text_rect.left - 40, text_rect.centery + 10),
                ],
            )

    instructions = [
        "Use UP/DOWN arrows to select a game",
        "Press ENTER to start the selected game",
        "Press ESC during a game to return to menu",
    ]

    instruction_font = pygame.font.SysFont(None, 24)
    for i, instruction in enumerate(instructions):
        instruction_text = instruction_font.render(instruction, True, (150, 150, 150))
        screen.blit(instruction_text, (20, SCREEN_HEIGHT - 80 + i * 25))


if __name__ == "__main__":
    main()
